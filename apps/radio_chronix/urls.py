from django.urls import path

from . import views


urlpatterns = [
    path('chronix_aggression/', views.chronix_aggression, name='chronix_aggression_index')
]