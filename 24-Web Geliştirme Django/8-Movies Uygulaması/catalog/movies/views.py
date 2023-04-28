from django.shortcuts import render
from .models import Movie
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    Movies = Movie.objects.all()
    context = {
        'movies': Movies

    }
    return render(request, 'movies/list.html', context)


def detail(request, movie_id):
    movies = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movies': movies
    }
    return render(request, 'movies/detail.html',context)


def search(request):
    return render(request, 'movies/search.html')
