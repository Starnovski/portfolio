from django.shortcuts import render, get_object_or_404
from .models import Type, Tech, Post, Category

# Create your views here.


def index(request):
    types = Type.objects.all()
    techs = Tech.objects.all()
    categories = Category.objects.all()
    return render(request, '../templates/index.html', {'types':types, 'techs':techs, 'categories':categories})


def category_posts(request, pk):
    categories = Category.objects.all()
    posts = Post.objects.filter(category = pk)
    categories = Category.objects.all()
    return render (request, '../templates/portfolio.html', {'posts':posts, 'categories':categories})

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render (request, '../templates/details.html', {'post':post})
