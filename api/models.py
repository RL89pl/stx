from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
        
class Book(models.Model):
    title = models.CharField(max_length=155, unique=True, db_index=True)
    authors = models.ManyToManyField(Author)
    published_date = models.PositiveIntegerField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    average_rating = models.PositiveIntegerField(blank=True, null=True)
    ratings_count = models.PositiveIntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

