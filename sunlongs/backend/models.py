from django.db import models
import ImageFilter

# Create your models here.

class TextInfo(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    content = models.TextField()
    tag = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class ImageInfo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images')
    display_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
