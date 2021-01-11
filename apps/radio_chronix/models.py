from django.db import models

from apps.radio_hub.models import Track


class ChronixAggressionTrack(models.Model):
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

# Cannot acces data with request like in others. To be done in future.
"""class ChronixRadioTrack(models.Model):
    played_time = models.DateTimeField('date published')
    track = models.ForeignKey(Track, on_delete=models.PROTECT)

    def __repr__(self):
        return f"{self.__class__.__name__} - ({self.track})"""
