# Generated by Django 3.2.11 on 2022-01-27 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='gif',
        ),
    ]
