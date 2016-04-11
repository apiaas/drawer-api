from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = ('is_staff', 'is_active', 'date_joined',
                            'is_superuser', 'groups', 'user_permissions',
                            'last_login')
