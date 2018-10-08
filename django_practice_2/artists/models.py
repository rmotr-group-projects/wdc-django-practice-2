from django.db import models


GENRE_CHOICES = (
    ("soul", "soul"),
    ("rock", "rock"),
    ("pop", "pop"),
)

class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    artistic_name = models.CharField(max_length=255)
    picture_url = models.URLField()
    popularity = models.IntegerField()
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES, null=True)


class Song(models.Model):
    artist_id = models.IntegerField()
    title = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
