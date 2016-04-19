# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_remove_document_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'permissions': (('can_view_document', 'Can view document'), ('can_delete_document', 'Can delete document'), ('can_change_document', 'Can change document'))},
        ),
        migrations.RemoveField(
            model_name='document',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='document',
            name='processed',
        ),
        migrations.RemoveField(
            model_name='document',
            name='processing_start_time',
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='filename',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='processed_text',
            field=models.TextField(default=''),
        ),
    ]