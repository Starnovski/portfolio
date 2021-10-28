from django.contrib import admin
from .models import Type, Tech, Post, Category, Contact
# Register your models here.

admin.site.register(Type)
admin.site.register(Tech)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Contact)
