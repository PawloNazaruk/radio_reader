from django.shortcuts import render

from .models import Track


def index(request):
    tracks = Track.objects.all()
    content = {
        'tracks': tracks
    }
    return render(request, 'radio_hub/basic.html', content)

