from ast import arg
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + " || " + str(self.author)

    def get_absolute_url(self):
        # return reverse( 'details', args=(str(self.id)) )
        return reverse('home')