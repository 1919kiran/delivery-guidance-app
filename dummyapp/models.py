from django.db import models
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your models here.
class AuthModel(models.Model):
    image = models.FileField(upload_to='media', default='settings.MEDIA_ROOT/abba.png')
