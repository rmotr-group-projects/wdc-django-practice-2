from artists.models import Artist, Song


def task_1_artists_filter_by_popularity():
    """Should return all artists that have more than 80 popularity"""
    return Artist.objects.all().filter(popularity__gt='80')


def task_2_artists_get_by_artistic_name():
    """Should return the artist which artistic name is Jimi Hendrix"""
    return Artist.objects.get(artistic_name="Jimi Hendrix")


def task_3_songs_delete():
    """Should delete all songs that contain any letter 'a' in its title"""
    return Song.objects.all().filter(title__icontains='a').delete()


def task_4_artists_create_song():
    """Should create a new song for Ed Sheeran artist"""
    Song.objects.create(artist_id="9", title="Hokey Song", album_name="Lame-oh Ed")


def task_5_artists_order_by_popularity():
    """Should return all artists ordered by popularity"""
    return Artist.objects.order_by('popularity')


def task_6_song_edit_album():
    """Should take the song with title 'Superstition' and update its album name with any other name"""
    Song.objects.filter(title='Superstition').update(album_name='Something Else')


def task_7_song_counter():
    """Should return the amount of songs stored in the database"""
    return len(Artist.objects.all())
