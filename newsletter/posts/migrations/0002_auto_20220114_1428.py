# Generated by Django 3.2.11 on 2022-01-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentlike',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='commentlike',
            name='laugh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='commentlike',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postlike',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postlike',
            name='laugh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postlike',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
