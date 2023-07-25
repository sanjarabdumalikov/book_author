from rest_framework import serializers
from .models import bookModel, authorModel, bookcategoryModel
from django.shortcuts import get_object_or_404


class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = authorModel
        fields = ('name', 'fname', 'date_of_birth', 'country')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookModel
        fields = ('id', 'author', 'name', 'category', 'page', 'price')