from django.db import models
from tastypie.resources import ModelResource
from movies.models import *
# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resources_name = 'movies'
        excludes = ['date_created']
