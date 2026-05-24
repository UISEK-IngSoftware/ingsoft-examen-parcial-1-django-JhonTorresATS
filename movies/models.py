from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('A', 'Accion'),
        ('H', 'Horror'),
        ('T', 'Thriller'),
        ('C', 'Comedia'),
        ('R', 'Romance'),
        ('F', 'Ciencia Ficcion'),
    ]
    name = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, null=False)
    director = models.CharField(max_length=30, null=False)
    date = models.DateField(null=False)
    synopsis = models.TextField(max_length=240, null=False)
    picture = models.ImageField(upload_to='movie_pictures/', null=True, blank=True)


    def __str__(self):
        return f"{self.name} {self.director}"