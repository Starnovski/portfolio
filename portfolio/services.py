from django.shortcuts import render
from .models import Category
# Create your views here.


def get_categories():
    categories = Category.objects.all()

    return categories
