from django.conf.urls import patterns, url
from django.contrib.auth.views import logout
from apiauth.views import apilogin, obtain_auth_token, apiregister

app = '^api/'

urlpatterns = [
    url(app + 'login/$', apilogin, name='api_login'),
    url(app + 'logout/$', logout, name='api_logout'),
    url(app + 'auth-token/', obtain_auth_token, name='api-token-auth'),
    url(app + 'register/', apiregister, name='api_register'),
    #url(app + 'auth-token-portal/', 'auth_token_portal', name='auth-token-portal'),
    #url(app + 'docs/', 'documentation', name='api-documentation'),
]
#
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#
#     # client
#     url(r'', include('client.urls')),
#     #apilogin
#     url(r'', include('apiauth.urls')),
#
#     url(r'^admin/', admin.site.urls),
# ]
