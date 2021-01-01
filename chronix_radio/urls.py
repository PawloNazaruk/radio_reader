from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('chronix_aggression/', views.chronix_aggression, name="chronix_aggression"),
]