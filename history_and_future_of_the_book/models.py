from django.db import models
from django.utils import timezone

import fileinput
import xlrd


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

DaveBook = xlrd.open_workbook("/Users/apple/Desktop/Workbook1.xlsx")
DaveSpreadsheet = DaveBook.sheet_by_index(0)

class TableManager(models.Manager):
    def create_table(self):
        table = self.create(file_position='0')
        file_position = DaveSpreadsheet.col_slice(colx=0, start_rowx=1, end_rowx=None)
        kwicl = DaveSpreadsheet.col_slice(colx=1, start_rowx=1, end_rowx=None)
        keyword = DaveSpreadsheet.col_slice(colx=2, start_rowx=1, end_rowx=None)
        kwicr = DaveSpreadsheet.col_slice(colx=3, start_rowx=1, end_rowx=None)
        choice1 = DaveSpreadsheet.col_slice(colx=4, start_rowx=1, end_rowx=None)
        choice2 = DaveSpreadsheet.col_slice(colx=5, start_rowx=1, end_rowx=None)
        choice3 = DaveSpreadsheet.col_slice(colx=6, start_rowx=1, end_rowx=None)
        correct_choice = DaveSpreadsheet.col_slice(colx=7, start_rowx=1, end_rowx=None)
        return table


class Table(models.Model):
    file_position = models.CharField(max_length=200)
    kwicl = models.TextField()
    keyword = models.CharField(max_length=200)
    kwicr = models.TextField()
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=200)
    objects = TableManager()



    def __str__(self):
        return str(self.file_position)

table = Table.objects.create_table()

    

    
    

