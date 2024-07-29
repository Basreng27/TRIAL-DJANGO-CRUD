from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .controller import *
from .form import *

# Create your views here.
def default_page(request):
    # return HttpResponse("Ini Page Default")
    return render(request, 'template/dashboard.html')

def genre_list(request):
    genre = Genre.objects.all()

    data = {
        'title': 'List Genre',
        'data': genre
    }

    return render(request, 'genre/list.html', data)

def genre_create(request, id=None):
    if id:
        genre = get_object_or_404(Genre, id=id)
        form = GenreForm(request.POST or None, instance=genre)
    else:
        form = GenreForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('genre_list')

    data = {
        'title': "Create Genre" if not id else "Edit Genre",
        'form': form,
    }

    return render(request, 'genre/create.html', data)

def genre_delete(request, id:int):
    genre = get_object_or_404(Genre, id=id)

    if request.method == 'POST':
        genre.delete()
    
    return redirect('genre_list')

def comic_list(request):
    comic = Comic.objects.all()

    data = {
        'title': 'List Comic',
        'data': comic
    }

    return render(request, 'comic/list.html', data)

def comic_create(request, id=None):
    if id:
        comic = get_object_or_404(Comic, id=id)
        form = ComicForm(request.POST or None, instance=comic)
    else:
        form = ComicForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('comic_list')

    data = {
        'title': "Create Comic",
        'form': form
    }

    return render(request, 'comic/create.html', data)

def comic_delete(request, id:int):
    comic = get_object_or_404(Comic, id=id)

    if request.method == 'POST':
        comic.delete()
    
    return redirect('comic_list')