from django.db import models
from django.core.validators import RegexValidator


class Type(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/types/')

    def __str__(self):
        return self.title

#There is probably no need to use a model for only
#one email and one phone number, but I wanted to try
#validators and regexes
class Contact(models.Model):
    mail = models.CharField(max_length=255, validators=[RegexValidator('^\w+@([\w-]+\.)+[\w-]{2,4}$', message='Doesnt fit email pattern'), ])
    phone = models.CharField(max_length=9, validators=[RegexValidator('^\d+$', message='Doesnt fit phone pattern'), ])

    def __str__(self):
        return self.mail


class Tech(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/techs/')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, related_name = 'posts', on_delete = models.CASCADE,)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/posts/')
    lead = models.CharField(max_length=255)
    body = models.TextField()


    def __str__(self):
        return self.title
