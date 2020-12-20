from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "chronix_aggression/index.html")
