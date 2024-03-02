from django.db import models

# Create your models here.
class FileModel(models.Model):
    file = models.FileField(upload_to = "cvs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

class descript(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    