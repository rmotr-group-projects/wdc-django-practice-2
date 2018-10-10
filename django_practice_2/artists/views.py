from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Artist, Song


def artists(request):
    artists = Artist.objects.all()

    first_name = request.GET.get('first_name')
    if first_name:
        artists = artists.filter(first_name__icontains=first_name)

    popularity = request.GET.get('popularity')
    if popularity:
        artists = artists.filter(popularity__gte=popularity)

    genre = request.GET.get('genre')
    if genre:
        artists = artists.filter(genre__icontains=genre)

    return render(request, 'artists.html',{'artists': artists})

def artist(request, artist_id):
    try:
        artist = Artist.objects.get(pk=artist_id)
    except:
        return HttpResponseNotFound("You've selected an artist that doesn't exist")
    return render(request, 'artist.html', {'artist': artist})


def songs(request, artist_id=None):
    songs = Song.objects.all()

    if artist_id:
        if artist_id in Artist.objects.all().values_list('id', flat=True):
            songs = songs.filter(artist_id=artist_id)
        else:
            return HttpResponseNotFound("You've selected an artist that doesn't exist")

    title = request.GET.get('title')
    if title:
        songs = songs.filter(title__icontains=title)

    for song in songs:
        artist = Artist.objects.get(id=song.artist_id)
        song.artist = artist
    return render(request, 'songs.html', {'songs': songs})
