from rest_framework import generics, status
from guardian.shortcuts import get_objects_for_user
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=serializer.validated_data, user=request.user)
            up_file = request.FILES['fileUpload']
            destination = open('media/' + up_file.name, 'wb+')
            for chunk in up_file.chunks():
                destination.write(chunk)
                destination.close()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

document_list = DocumentList.as_view()


class DocumentDetail(generics.RetrieveUpdateAPIView):
    """
    Document detail.
    """
    model = Document
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
