"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps.radio_hub import views as radio_hub_views

import apps.radio_chronix.managment.commands.radio_chronix_scraper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('radio_hub/index/', radio_hub_views.index, name="radio_hub_index"),
    path('radio_hub/radio_chronix/', include('apps.radio_chronix.urls')),
]
