from django.shortcuts import render
from .models import Track, ChronixAggressionTrack, ChronixGritTrack, ChronixMetalTrack


def chronix_history(requests):
    tracks_aggression = ChronixAggressionTrack.objects.all().order_by('-played_time')[:5]
    current_track_aggression = tracks_aggression[0]
    last_four_aggression = tracks_aggression[1:]

    tracks_grit = ChronixGritTrack.objects.all().order_by('-played_time')[:5]
    current_track_grit = tracks_grit[0]
    last_four_grit = tracks_grit[1:]

    tracks_metal = ChronixMetalTrack.objects.all().order_by('-played_time')[:5]
    current_track_metal = tracks_metal[0]
    last_four_metal = tracks_metal[1:]

    context = {
        'current_track_aggression': current_track_aggression,
        'current_track_grit': current_track_grit,
        'current_track_metal': current_track_metal,
        'last_four_aggression': last_four_aggression,
        'last_four_grit': last_four_grit,
        'last_four_metal': last_four_metal,
    }
    return render(requests, 'chronix_radio/chronix_history.html', context)

def index(request):
    tracks = Track.objects.all()
    context = {
        "tracks": tracks,
    }
    return render(request, "chronix_radio/index.html", context)


def chronix_aggression(request):
    tracks_aggression = ChronixAggressionTrack.objects.all()
    context = {
        "tracks_aggression": tracks_aggression
    }
    return render(request, "chronix_radio/chronix_aggression.html", context)