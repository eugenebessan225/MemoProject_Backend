from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

class PersonViewset(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class BookViewset(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
