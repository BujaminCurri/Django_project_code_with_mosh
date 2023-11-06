from django.contrib import admin
from .models import *
# Register your models here.


class GenreAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']


admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):

    exclude = ('date_created',)
    list_display = ('title', 'number_in_stock', 'daily_rate')


admin.site.register(Movie, MovieAdmin)
