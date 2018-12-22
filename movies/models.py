from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    release_date = models.DateTimeField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Review(models.Model):
    summary = models.CharField(max_length=2000)
    date_created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)