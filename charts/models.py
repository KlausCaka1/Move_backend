from django.db import models


class ExampleModel(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

