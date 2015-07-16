# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

import csv



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



