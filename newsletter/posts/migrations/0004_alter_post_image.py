# Generated by Django 3.2.11 on 2022-01-25 15:05

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_suggestion_suggestioncomment_suggestionvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='posts'),
        ),
    ]
