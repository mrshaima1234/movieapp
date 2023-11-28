from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, "index.html", context)


def detail(request, movie_id):
    return HttpResponse("this is movie no %s" % movie_id)


def getMovie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "movie_detail.html", {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        descr = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['image']

        movie = Movie(name=name, desc=descr, year=year, img=img)
        movie.save()
    return render(request, 'add.html')


def updateMovie(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'forms': form, 'movie': movie})

def delete(request,id):
    if request.method=='POST':
        movieid= Movie.objects.get(id=id)
        movieid.delete()
        return redirect('/')
    return render(request,'delete.html')

