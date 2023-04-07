from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_http_methods
# Create your views here.
@require_http_methods(['GET'])
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)
@require_http_methods(['GET'])
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {'movie':movie}
    return render(request, 'movies/detail.html', context)
@require_http_methods(['POST','GET'])
def create(request):
    if request.method=="POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {'form':form}
    return render(request, 'movies/create.html', context)
@require_http_methods(['POST'])
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
@require_http_methods(['POST','GET'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method=="POST":
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {'form':form, 'movie':movie}
    return render(request, 'movies/update.html', context)
