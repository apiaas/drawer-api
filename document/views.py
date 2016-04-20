from rest_framework import generics, status
from guardian.shortcuts import get_objects_for_user
from .models import Document
from .serializers import DocumentSerializer, DocumentIndexSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView

from haystack.query import SearchQuerySet

class DocumentList(generics.ListCreateAPIView):
    """
    Document list.
    """
    permission_classes = (IsAuthenticated,)
    model = Document
    serializer_class = DocumentSerializer

    def get_queryset(self):
        documents_qs = get_objects_for_user(self.request.user, Document.CAN_VIEW, Document)
        return documents_qs

    def post(self, request, *args, **kwargs):

        up_file = request.FILES['fileUpload']
        file_path = 'media/' + up_file.name
        destination = open(file_path, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()
        data = request.data.copy()
        data['filename'] = up_file.name
        data['path'] = file_path
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.create(validated_data=serializer.validated_data, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

document_list = DocumentList.as_view()


class DocumentDetail(generics.RetrieveUpdateAPIView):
    """
    Document detail.
    """

    serializer_class = DocumentSerializer

    def get_queryset(self):
        return Document.objects.all()

    def delete(self, request, pk, format=None):
        try:
            doc = Document.objects.get(pk=pk)
            doc.delete()
        except Document.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        return Response(status=status.HTTP_204_NO_CONTENT)

document_detail = DocumentDetail.as_view()


# class DocumentSearchView(HaystackViewSet):
#     def wasd(asd, asd2):
#         return Response(data={'asd': 3242}, status=status.HTTP_200_OK)
#     # `index_models` is an optional list of which models you would like to include
#     # in the search result. You might have several models indexed, and this provides
#     # a way to filter out those of no interest for this particular view.
#     # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
#     index_models = [Document]
#
#     serializer_class = DocumentIndexSerializer
#
# document_search = DocumentSearchView.as_view({'get': 'wasd'})

class SearchView(ListModelMixin, HaystackGenericAPIView):
    serializer_class = DocumentIndexSerializer
    model = Document

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

document_search = SearchView.as_view()

