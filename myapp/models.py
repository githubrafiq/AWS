from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    image = models.FileField(upload_to='post_image/')
