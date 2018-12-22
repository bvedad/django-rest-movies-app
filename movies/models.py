from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    release_date = models.DateTimeField()
    genre = models.ManyToManyField(Genre)
