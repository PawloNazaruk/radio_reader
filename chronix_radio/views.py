from django.shortcuts import render
from .models import Track
from pprint import pprint
# Create your views here.

def index(request):
    tracks = Track.objects.all()
    context = {
        "tracks": tracks,
        "temp": "asd",
    }
    pprint(context)
    return render(request, "chronix_radio/index.html", context)
