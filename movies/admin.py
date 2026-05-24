from django.contrib import admin
from .models import Movie

# Register your models here.
admin.site.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass