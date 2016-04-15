from rest_framework import serializers
from guardian.shortcuts import assign_perm
from .models import Document
from django.db import transaction


class DocumentSerializer(serializers.ModelSerializer):

    def create(self, validated_data, user):
        with transaction.atomic():
            obj = super(DocumentSerializer, self).create(validated_data)
            assign_perm(Document.CAN_VIEW, user, obj)
            assign_perm(Document.CAN_DELETE, user, obj)
            assign_perm(Document.CAN_UPDATE, user, obj)
            return obj

    class Meta:
        model = Document
        extra_kwargs = {'path': {'write_only': True}, 'filename': {'write_only': True}}
