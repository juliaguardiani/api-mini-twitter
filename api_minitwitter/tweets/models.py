from django.db import models
from uuid import uuid4

# Create your models here.

#Para não correr o riscor de existir dois arquivos de img com o msm nome.
def upload_image_tweet(instance, filename):
    return f"{instance.id_tweet}-{filename}"


class Tweets(models.Model):
    id_tweet = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tweet = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_image_tweet, blank=True, null=True)
