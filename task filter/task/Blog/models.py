from django.db import models
from Author.models import Author 


# Create your models here.

class Post (models.Model):

    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    Pub_date = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)


