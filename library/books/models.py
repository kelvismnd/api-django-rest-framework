from django.db import models
from uuid import uuid4
# Create your models here.

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=100)
    release_year = models.IntegerField()
    state = models.CharField(max_length=100)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)