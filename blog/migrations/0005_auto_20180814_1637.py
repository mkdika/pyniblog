# Generated by Django 2.1 on 2018-08-14 09:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='Post',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='comment_body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
