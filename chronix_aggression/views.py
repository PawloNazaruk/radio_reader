from django.shortcuts import render
from .models import Song
from pprint import pprint
# Create your views here.

def index(request):
    songs = Song.objects.all()
    context = {
        "songs": songs,
        "temp": "asd",
    }
    pprint(context)
    return render(request, "chronix_aggression/index.html", context)
