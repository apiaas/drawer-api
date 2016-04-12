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
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

document_list = DocumentList.as_view()

class DocumentDetail(generics.GenericAPIView):
    """
    In response you get:
    token -- key 48 character
    expires -- in seconds
    expires_date -- after this date the token is invalid
    user -- User serializer object
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = DocumentSerializer
    model = Document

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, pk):
        instance = Document.objects.get(pk=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.update(instance=instance, validated_data=serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

document_detail = DocumentDetail.as_view()
