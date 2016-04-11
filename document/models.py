from django.db import models


# Create your models here.
class Document(models.Model):
    filename = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    description = models.TextField()
    processed_text = models.TextField()
    deleted = models.BooleanField()
    processed = models.BooleanField(default=False)
    processing_start_time = models.IntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     user_id = re