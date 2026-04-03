from django.db import models

class Artist(models.Model):
    class ArtistType(models.TextChoices):
        SOLO = "solo", "Solo Artist"
        BAND = "band", "Band"
        DJ = "dj", "DJ"
        OTHER = "other", "Other"

    name = models.CharField(max_length=255)
    artist_type = models.CharField(
        max_length=10,
        choices=ArtistType.choices,
        default=ArtistType.SOLO,
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Founder(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=255)
    founding_year = models.PositiveIntegerField(null=True, blank=True)
    founders = models.ManyToManyField(Founder, related_name ="labels", blank=True)

    def __str__(self):
        return self.name
    

class Record(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="records")
    genres = models.ManyToManyField(Genre, related_name="records", blank=True)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True, blank=True, related_name="records")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"
