from django.conf.urls import url
from document.views import document_list
from document.views import document_detail
from document.views import document_search


urlpatterns = [

    url('api/document/document/$', document_list, name='api_document_list'),
    url('api/document/document/(?P<pk>\d+)/$', document_detail, name='api_document_detail'),
    url(r'^search/', document_search, name='document_search'),
]
