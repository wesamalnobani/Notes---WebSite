from django.contrib import admin
from .models import Notes
# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_filter =['active', 'created', 'tags']
    list_display = ['title', 'created', 'active' ]
    search_fields = ['title']



admin.site.register(Notes, NotesAdmin)
