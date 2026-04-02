from django.db import models

class Artist(models.Model):
    class ArtistType(models.TextChoices):
        SOLO = "solo", "Solo Artist"
        BAND = "band", "Band"
        DJ = "dj", "DJ"
        OTHER = "other", "Other"

    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=10,
        choices=ArtistType.choices,
        default=ArtistType.SOLO,
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Record(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='records')
    genre = models.CharField(max_length=100, blank=True)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"
