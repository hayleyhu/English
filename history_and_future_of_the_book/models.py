# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

import csv


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Table(models.Model):
    file_position = models.CharField(max_length=200)
    kwicl = models.TextField()
    keyword = models.CharField(max_length=200)
    kwicr = models.TextField()
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=200)

    def __str__(self):
        return str(self.file_position)


    
    

