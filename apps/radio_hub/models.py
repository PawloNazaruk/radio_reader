from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    img = models.ImageField(upload_to="covers", blank=True)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.title == other.title and \
                    self.artist == other.artist and \
                    self.album == other.album
        else:
            return False

    def __str__(self):
        return f"{self.__class__.__name__}({self.title},{self.artist},{self.album},{self.pk})"

