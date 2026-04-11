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
    artist = ArtistSerializer(read_only=True)
    label = LabelSerializer(read_only = True)

    class Meta:
        model = Record
        fields = [
            "id",
            "title",
            "artist",
            "genres",
            "release_year",
            "label",
            "created_at",
        ]
