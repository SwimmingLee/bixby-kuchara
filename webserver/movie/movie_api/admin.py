from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    print('movie start')
    #list_display = ['id', 'moiveName', 'movieRoom']
    #list_editable = ['moiveName', 'movieRoom']

admin.site.register(Movie, MovieAdmin)
# Register your models here.
