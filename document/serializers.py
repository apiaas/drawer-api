from rest_framework import serializers
from guardian.shortcuts import assign_perm, get_objects_for_user
from .models import Document
from django.db import transaction


class DocumentSerializer(serializers.ModelSerializer):
    processed_text = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    description = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)

    # def validate(self, attrs):
    #     processed_text = attrs.get('processed_text')
    #     description = attrs.get('description')

    def create(self, validated_data, user):
        # (self, **kwargs):
        with transaction.atomic():
            # user = self.context['request'].user
            obj = super(DocumentSerializer, self).create(validated_data)
            assign_perm(Document.CAN_VIEW, user, obj)
            assign_perm(Document.CAN_DELETE, user, obj)
            assign_perm(Document.CAN_UPDATE, user, obj)
            return obj

    # def update(self):
    def update(self, instance, validated_data):
        return super(DocumentSerializer, self).save(validated_data)


    class Meta:
        model = Document
        read_only_fields = ('filename', 'description', 'processed_text')
