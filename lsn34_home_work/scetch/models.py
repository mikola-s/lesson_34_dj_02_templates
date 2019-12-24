from django.db import models

# Create your models here.

from django.db import models


class Test_Model(models.Model):
    title = models.CharField()
    email = models.EmailField()
    publication_date = models.DateField()
