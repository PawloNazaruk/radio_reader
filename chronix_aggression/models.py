from django.db import models


class Song(models.Model):
    track_text = models.CharField(max_length=100)
    artist_text = models.CharField(max_length=100)
    album_text = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True)
    played_at = models.DateTimeField('date published')
    is_favourite = models.BooleanField(default=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.track_text} - {self.artist_text})"
