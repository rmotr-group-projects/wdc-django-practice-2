from artists.models import Artist, Song


def task_1_artists_filter_by_popularity():
    """Should return all artists that have more than 80 popularity"""
    return Artist.objects.filter(popularity__gt=80)


def task_2_artists_get_by_artistic_name():
    """Should return the artist which artistic name is Jimi Hendrix"""
    return Artist.objects.get(artistic_name="Jimi Hendrix")


def task_3_songs_delete():
    """Should delete all songs that contain any letter 'a' in its title"""
    Song.objects.filter(title__icontains='a').delete()


def task_4_artists_create_song():
    """Should create a new song for Ed Sheeran artist"""
    sheeran_id = Artist.objects.get(first_name__icontains="ed").id
    Song(title="foo", album_name="bar", artist_id=sheeran_id).save()


def task_5_artists_order_by_popularity():
    """Should return all artists ordered by popularity"""
    return Artist.objects.all().order_by("popularity")


def task_6_song_edit_album():
    """Should take the song with title 'Superstition' and update its album name with any other name"""
    superstition = Song.objects.get(title='Superstition')
    superstition.album_name = "My Beautiful Dark Twisted Fantasy"
    superstition.save()


def task_7_song_counter():
    """Should return the amount of songs stored in the database"""
    return Song.objects.count()
