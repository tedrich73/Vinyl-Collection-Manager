from django.contrib import admin
from .models import Artist, Record, Label, Genre

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "artist_type")
    search_fields = ("name",)
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "release_year")
    search_fields = ("title", "artist__name",)
    filter_horizontal = ("genres",)
