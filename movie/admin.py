from django.contrib import admin
from .models import Movie,Review

# Register your models here.
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title','description')
#
# admin.site.register(Movie,MovieAdmin)


admin.site.register(Movie)
admin.site.register(Review)
