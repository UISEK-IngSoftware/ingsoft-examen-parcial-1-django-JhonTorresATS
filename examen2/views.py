from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Movies

def index(request):
    movies = Movies.objects.all()
    template = loader.get_template('index.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))


def movie(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    template = loader.get_template('display_movie.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))
