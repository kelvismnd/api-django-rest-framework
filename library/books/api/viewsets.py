from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()

