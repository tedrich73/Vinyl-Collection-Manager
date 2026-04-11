from rest_framework import serializers
from .models import Record, Artist, Label


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            "id",
            "name",
            "artist_type",
            "description",
            ]
    
class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = [
            "id",
            "name",
            "founding_year",
            "founders",
        ]

class RecordSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source="artist.name", read_only=True)
    label_name = serializers.CharField(source="label.name", read_only=True)
    genre_names = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = [
            "id",
            "title",
            "artist",
            "artist_name",
            "genres",
            "genre_names",
            "release_year",
            "label",
            "label_name",
            "created_at",
        ]
    
    def get_genre_names(self, obj):
        return [genre.name for genre in obj.genres.all()]
