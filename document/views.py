from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Document
from .serializers import DocumentSerializer
# Create your views here.
class DocumentList(generics.ListCreateAPIView):
    """
    Client list.
    """
    model = Document
    serializer_class = DocumentSerializer

    def get_queryset(self):
        # if self.request.user.is_superuser:
        #     return Document.objects.exclude(id=ANONYMOUS_USER_ID)
        return Document.objects.all()

document_list = DocumentList.as_view()

# class DocumentDetail(generics.GenericAPIView):
#     """
#     In response you get:
#     token -- key 48 character
#     expires -- in seconds
#     expires_date -- after this date the token is invalid
#     user -- User serializer object
#     """
#     permission_classes = ()
#     serializer_class = DocumentSerializer
#     model = Document
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#
# document_detail = DocumentDetail.as_view()
