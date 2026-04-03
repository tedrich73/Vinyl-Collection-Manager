from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.select_related("artist", "label").all()
    serializer_class = RecordSerializer
