from django.db import models


# Create your models here.
class Document(models.Model):
    CAN_VIEW = 'can_view_document'
    CAN_DELETE = 'can_delete_document'
    CAN_UPDATE = 'can_change_document'

    filename = models.CharField(max_length=100, default='')
    path = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    processed_text = models.TextField(default='')
    # deleted = models.BooleanField()
    # processed = models.BooleanField(default=False)
    # processing_start_time = models.IntegerField(default=0)

    class Meta:
        permissions = (
            ('can_view_document', 'Can view document'),
            ('can_delete_document', 'Can delete document'),
            ('can_change_document', 'Can change document'),
        )
