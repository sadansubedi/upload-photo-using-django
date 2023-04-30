from django.db import models

# Create your models here.

#when we are working with images uploader we must install Pillow by  python -m pip install Pillow
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")# here upload_to="myimage" create myimage folder (media file) and store all images
    date = models.DateTimeField(auto_now_add=True)