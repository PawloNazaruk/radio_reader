from django.shortcuts import render
from .models import Track


def index(request):
    tracks = Track.objects.all()
    context = {
        "tracks": tracks,
    }
    return render(request, "chronix_radio/index.html", context)
