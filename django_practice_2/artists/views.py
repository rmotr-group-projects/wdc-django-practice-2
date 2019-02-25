from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound

from .models import Artist, Song


def artists(request):

    artists = Artist.objects.all()

    if 'first_name' in request.GET:
        first_name = request.GET['first_name']
        if first_name:
            artists = artists.filter(first_name__icontains=first_name)


    if 'popularity' in request.GET:
        popularity = request.GET['popularity']
        if popularity:
            artists = artists.filter(popularity__gte=popularity)


    if 'genre' in request.GET:
        genre = request.GET['genre']
        if genre:
            artists = artists.filter(genre__contains=genre)


    context = {
        'artists': artists
    }

    return render(request, "artists.html", context)


def artist(request, artist_id):

    artist = get_object_or_404(Artist, id=artist_id)

    context = {
        'artist': artist
    }

    return render(request, 'artist.html', context)


def songs(request, artist_id=None):

    songs = Song.objects.all()

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            songs = songs.filter(title__contains=title)


    for song in songs:
        artist = Artist.objects.get(id=song.artist_id)
        song.artist = artist


    context = {
        'songs': songs
    }

    return render(request, 'songs.html', context)