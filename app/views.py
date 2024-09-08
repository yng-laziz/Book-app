from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.


class AutorView(viewsets.ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializar


class BookView(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializar


class CategoriesView(viewsets.ModelViewSet):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializar