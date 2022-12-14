from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Response(models.Model):
    slackUsername = models.CharField(max_length = 50)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername