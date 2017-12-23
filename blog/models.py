from django.db import models
from __future__ import unicode_literals

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=32,default='title')
    contrnt=models.TextField(null=True)