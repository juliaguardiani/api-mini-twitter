# Generated by Django 4.0.1 on 2022-01-23 23:45

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=tweets.models.upload_image_tweet),
        ),
    ]
