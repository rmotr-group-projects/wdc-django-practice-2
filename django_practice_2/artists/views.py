from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Artist, Song


def artists(request):
    ## Get the value of a GET variable with name 'page', and if it doesn't exist, return 1
    name = request.GET.get('first_name')
    pop = request.GET.get('popularity')
    genre = request.GET.get('genre')
    artists = Artist.objects.all() ## gets objects from def(artist(param, param2))
    
    if name:
        artists = artists.filter(first_name__icontains=name)
    if pop:
        ## gte means greater than or equal to
        artists = artists.filter(popularity__gte=pop)
    if genre:
        artists = artists.filter(genre=genre)
    
    if not artists.exists():
            return HttpResponseNotFound("<h1>This world is devoid of artists</h1>")
    return render(request, "artists.html", context={'artists':artists})


def artist(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id).get()
    except Artist.DoesNotExist:
        return HttpResponseNotFound("Sorry couldn't find that!")
        
    return render(request, 'artist.html', context={'artist':artist})


def songs(request, artist_id=None):
    songs = Song.objects.all()
    title = request.GET.get('title')
    
    if artist_id:
        songs = songs.filter(artist_id=artist_id)
    
    if title:
        songs = songs.filter(title__icontains=title)
    
    for song in songs:
        artist = Artist.objects.get(id=song.artist_id)
        song.artist = artist
        
    return render(request, 'songs.html', context={'songs':songs})
