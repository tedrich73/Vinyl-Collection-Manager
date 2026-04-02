from django.contrib import admin
from .models import Artist, Record

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "artist_type")
    search_fields = ("name",)
    
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "release_year")
