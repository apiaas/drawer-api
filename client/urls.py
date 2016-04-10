from django.conf.urls import patterns, url
from client.views import client_detail, client_list


urlpatterns = [
    # 'client.views',

    # client
    url('api/client/client/$', client_list, name='api_client_list'),
    url('api/client/client/(?P<pk>\d+)/$', client_detail,
        name='api_client_detail'),
]
