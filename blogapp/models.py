from django.db import models


# Create your models here.
class blog(models.Model):
    blog_id=models.IntegerField()
    blogname=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='picture')
