from django.db import transaction
from django.db.models import Q

# from guardian.shortcuts import assign, get_objects_for_user
from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = ('is_staff', 'is_active', 'date_joined',
                            'is_superuser', 'groups', 'user_permissions',
                            'last_login')
