import re

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})


def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'display_movie.html', {'movie': movie})
