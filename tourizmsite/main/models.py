from django.db import models


class Mymodel(models.Model):
    col = models.CharField(max_length=10)
