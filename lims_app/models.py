from django.db import models

# Create your models here.
class Reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id = models.IntegerField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.TextField()
    active = models.BooleanField(default=True)
    books = models.ManyToManyField('Book', related_name='readers')

class Book(models.Model):
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30, default='education')