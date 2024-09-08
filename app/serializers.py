from rest_framework import serializers
from .models import *

class AuthorSerializar(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'

class BookSerializar(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'


class CategoriesSerializar(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = '__all__'