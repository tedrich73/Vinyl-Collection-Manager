from rest_framework.routers import DefaultRouter
from .views import RecordViewSet, ArtistViewSet, LabelViewSet

router = DefaultRouter()
router.register("records", RecordViewSet, basename="record")
router.register("artists", ArtistViewSet, basename="artist")
router.register("labels", LabelViewSet, basename="label")

urlpatterns = router.urls