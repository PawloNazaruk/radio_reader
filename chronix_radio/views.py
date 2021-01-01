from django.shortcuts import render
from .models import Track, ChronixAggressionTrack


def index(request):
    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    tracks = Track.objects.all()
    context = {
        "tracks": tracks,
    }
    return render(request, "chronix_radio/index.html", context)


def chronix_aggression(request):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    tracks_aggression = ChronixAggressionTrack.objects.all()
    context = {
        "tracks_aggression": tracks_aggression
    }
    return render(request, "chronix_radio/chronix_aggression.html", context)