from rest_framework import viewsets
from .models import Record, Artist, Label
from .serializers import RecordSerializer, ArtistSerializer, LabelSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.select_related("artist", "label").all()
    serializer_class = RecordSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
