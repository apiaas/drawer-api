# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from rest_framework import serializers
from client.models import Client


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, min_length=2)
    password = serializers.CharField(max_length=30, min_length=2)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError('Unable to login with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password"')


class ApiRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, min_length=2)

    def validate(self, attrs):
        username = attrs.get('username')
        if username:
            password = Client.objects.make_random_password()
            user = Client(username=username)
            user.set_password(password)
            user.save()
            return {'username': username, 'password': password}
        else:
            raise serializers.ValidationError('Must include "username"')
