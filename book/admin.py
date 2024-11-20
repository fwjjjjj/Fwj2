from django.contrib import admin
from .models import Book,Reviews
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
    search_fields = ['title','description']
    list_editable = ('description',)

admin.site.register(Book,BookAdmin)

# admin.site.register(Book)
admin.site.register(Reviews)