# Generated by Django 2.1 on 2018-08-15 06:11

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180815_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_body',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
