# Generated by Django 2.1.5 on 2019-03-06 11:19

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]
