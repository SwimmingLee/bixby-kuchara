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

from movies.movieapi import SearchMovieListWithPos
from movies.movieapi import SearchTheaterWithPos
from movies.movieapi import SearchTheaterOrderedScheduleWithPos
from movies.movieapi import SearchTheaterWithMoviePos
from movies.movieapi import SearchMovieScheduleWithMovieTheater
from movies.movieapi import SearchTimeOrderedScheduleWithPos
from movies.movieapi_test import SearchMegaboxMovie
from movies.movieapi_test import SearchLottecinemaMovie
from movies.movieapi_test import SearchCGVMovie
from movies.movieapi_test import Test
from movies.update import UpdateTheater

from movies.crawling import WebDriverInit


router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('movieschedules',MovieScheduleViewSet)
router.register('theaters',TheaterViewSet)

WebDriverInit()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('movie_api/searchMovieListWithPos/', SearchMovieListWithPos, name='SearchMovieListWithPos'),
    path('movie_api/searchMovieScheduleWithMovieTheater/', SearchMovieScheduleWithMovieTheater, name='SearchMovieScheduleWithMovieTheater'),
    path('movie_api/searchTheaterWithPos/', SearchTheaterWithPos, name='SearchTheaterWithPos'),
    path('movie_api/searchTheaterWithMoviePos/', SearchTheaterWithMoviePos, name='SearchTheaterWithMoviePos'),
    path('movie_api/searchTheaterOrderedScheduleWithPos/', SearchTheaterOrderedScheduleWithPos, name='SearchTheaterOrderedScheduleWithPos'),
    path('movie_api/searchTimeOrderedScheduleWithPos/', SearchTimeOrderedScheduleWithPos, name='SearchTimeOrderedScheduleWithPos'),
    path('movie_api/searchMegaboxMovie/', SearchMegaboxMovie, name='SearchMegaboxMovie'),
    path('movie_api/searchLottecinemaMovie/', SearchLottecinemaMovie, name='SearchLottecinemaMovie'),
    path('movie_api/searchCGVMovie/', SearchCGVMovie, name='SearchCGVMovie'),
    path('movie_api/test/', Test, name='Test'),
    path('movie_update/theater', UpdateTheater, name='UpdateTheater')
]
