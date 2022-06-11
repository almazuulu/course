from operator import mod
from pydoc import describe
from statistics import mode
from django.db import models
import uuid

class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    instructor = models.CharField(max_length=200, null=True, blank=True)
    rating = models.FloatField()
    price = models.FloatField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

