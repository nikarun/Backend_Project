from django.db import models

# Create your models here.
class URL(models.Model):
    url=models.URLField(null=True,blank=True)
    content=models.TextField(null=True,blank=True)
