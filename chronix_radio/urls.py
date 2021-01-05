from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),
    path('chronix_aggression/', views.chronix_aggression, name='chronix_aggression'),
    path('chronix_history/', views.chronix_history, name='chronix_history'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
