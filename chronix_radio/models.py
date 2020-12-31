from django.db import models


class Track(models.Model):
    FAVOURITE_CHOICES = [("T", "True"), ("F", "False")]
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    img = models.ImageField(blank=True)
    favourite = models.BooleanField(choices=FAVOURITE_CHOICES, blank=True, default=False)
    counter = models.IntegerField(default=1)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title} - {self.artist})"


class ChronixRadioTrack(models.Model):
    played_time = models.DateTimeField('date published')
    track = models.ForeignKey(Track, on_delete=models.PROTECT)

    def __repr__(self):
        return f"{self.__class__.__name__} - ({self.track})"


class ChronixGritTrack(models.Model):
    played_time = models.DateTimeField('date published')
    track = models.ForeignKey(Track, on_delete=models.PROTECT)

    def __repr__(self):
        return f"{self.__class__.__name__} - ({self.track})"


class ChronixMetalTrack(models.Model):
    played_time = models.DateTimeField('date published')
    track = models.ForeignKey(Track, on_delete=models.PROTECT)

    def __repr__(self):
        return f"{self.__class__.__name__} - ({self.track})"


class ChronixAggressionTrack(models.Model):
    played_time = models.DateTimeField('date published')
    track = models.ForeignKey(Track, on_delete=models.PROTECT)

    def __repr__(self):
        return f"{self.__class__.__name__} - ({self.track})"



