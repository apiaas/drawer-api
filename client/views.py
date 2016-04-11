from rest_framework import generics, viewsets

from api.settings import ANONYMOUS_USER_ID

from .models import Client
from .serializers import ClientSerializer


##########
# CLIENT #
##########
class ClientList(generics.ListAPIView):
    """
    Client list.
    """
    model = Client
    serializer_class = ClientSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.exclude(id=ANONYMOUS_USER_ID)
        return Client.objects.filter(id=self.request.user.id)


class ClientDetail(generics.RetrieveUpdateAPIView):
    """
    Client detail.
    """
    model = Client
    serializer_class = ClientSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.exclude(id=ANONYMOUS_USER_ID)
        return Client.objects.filter(id=self.request.user.id)


client_list = ClientList.as_view()
client_detail = ClientDetail.as_view()

# ViewSets define the view behavior.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
