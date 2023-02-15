from django.db import models

# Create your models here.

class regmodel(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username

class fileModel(models.Model):
    itemname=models.CharField(max_length=20)
    image=models.FileField(upload_to='new_app/static')


    