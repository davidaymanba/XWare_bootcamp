from django.db import models


# Create your models here.


class visitor (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    visit_date = models.DateTimeField()
    