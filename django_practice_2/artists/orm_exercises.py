from artists.models import Artist, Song


def task_1_artists_filter_by_popularity():
    artists = Artist.objects.all().filter(popularity__gt=80)
    return ( artists )


def task_2_artists_get_by_artistic_name():
    artist = Artist.objects.get(artistic_name='Jimi Hendrix')
    return ( artist )


def task_3_songs_delete():
    Song.objects.all().filter(title__contains='a').delete()


def task_4_artists_create_song():
    artist = Artist.objects.get(artistic_name='Ed Sheeran')
    Song.objects.create(
        artist_id = artist.id,
        title = 'new title',
        album_name = 'new album_name'
    )


def task_5_artists_order_by_popularity():
    artists = Artist.objects.all().order_by('popularity')
    return ( artists )


def task_6_song_edit_album():
    # song = Song.objects.get(title='Superstition')
    # song.album_name = 'new album_name'
    # song.save()
    Song.objects.filter(title='Superstition').update(album_name='new album_name')


def task_7_song_counter():
    """Should return the amount of songs stored in the database"""
    return ( Song.objects.count() )