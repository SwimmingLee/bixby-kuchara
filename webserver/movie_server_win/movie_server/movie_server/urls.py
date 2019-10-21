"""movie_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
from movies.views import MovieViewSet
from movies.views import MovieScheduleViewSet
from movies.views import TheaterViewSet
from movies.views import NamedPointStructureViewSet
from movies.views import movie_list
from movies.views import SearchWithPos
from movies.update import UpdateTheater

from movies.crawling import WebDriverInit
from movies.views import Test

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('movieschedules',MovieScheduleViewSet)
router.register('theaters',TheaterViewSet)
router.register('namedstructures',MovieScheduleViewSet)

WebDriverInit()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('movie_api/searchWithTheaterName/', movie_list, name='movie_list'),
    path('movie_api/searchWithPos/', SearchWithPos, name='SearchWithPos'),
    path('movie_api/test/', Test, name='Test'),
    path('movie_update/theater', UpdateTheater, name='UpdateTheater')
]
