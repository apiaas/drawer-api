# -*- coding: utf-8 -*-
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth import login
from django.utils import timezone
from django.conf import settings

from django.contrib.auth.models import Group
from client.serializers import ClientSerializer
from .models import Token
from .serializers import AuthTokenSerializer



class ApiLogin(generics.GenericAPIView):
    """
    In response you get "Set-Cookie" with session id, which can use in
    Session Authentication. And you get User serializer object.
    """
    permission_classes = ()
    model = settings.AUTH_USER_MODEL
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(dir(serializer))
            user = serializer.validated_data['user']
            login(request, user)
            return Response(ClientSerializer(user).data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ObtainAuthToken(generics.GenericAPIView):
    """
    In response you get:
    token -- key 48 character
    expires -- in seconds
    expires_date -- after this date the token is invalid
    user -- User serializer object
    """
    permission_classes = ()
    serializer_class = AuthTokenSerializer
    model = Token

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        #group = Group.objects.get(name='adminusers')
        if serializer.is_valid():
            user = serializer.validated_data['user']
            Token.objects.filter(user=user, expires__lt=timezone.now()).delete()
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key, 'expires': 2400,
                'expires_date': token.expires.strftime('%Y-%m-%d %H:%M:%S'),
                'user': ClientSerializer(user).data})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


#class AuthTokenPortal(generics.GenericAPIView):
    #"""
    #Token auth for portal users.
    #"""
    #permission_classes = ()
    #model = settings.AUTH_USER_MODEL
    #serializer_class = AuthTokenSerializer

    #def post(self, request):
        #serializer = self.serializer_class(data=request.DATA)
        #p = 'customers.portal_user'
        #if serializer.is_valid() and serializer.object['user'].has_perm(p) and not serializer.object['user'].is_superuser:
            #user = serializer.object['user']
            #Token.objects.filter(user=user, expires__lt=timezone.now()).delete()
            #token, created = Token.objects.get_or_create(user=user)

            #return Response({'token': token.key, 'expires': 2400,
                #'expires_date': token.expires.strftime('%Y-%m-%d %H:%M:%S'),
                #'user': ClientSerializer(user).data})
        #return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


apilogin = ApiLogin.as_view()
obtain_auth_token = ObtainAuthToken.as_view()
#auth_token_portal = AuthTokenPortal.as_view()





