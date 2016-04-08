from django.conf.urls import patterns, url
from django.contrib.auth.views import logout

app = '^api/'

urlpatterns = patterns('apiauth.views',
    url(app + 'login/$', 'apilogin', name='api_login'),
    url(app + 'logout/$', logout, name='api_logout'),
    url(app + 'auth-token/', 'obtain_auth_token', name='api-token-auth'),
    #url(app + 'auth-token-portal/', 'auth_token_portal', name='auth-token-portal'),
    #url(app + 'docs/', 'documentation', name='api-documentation'),
)
