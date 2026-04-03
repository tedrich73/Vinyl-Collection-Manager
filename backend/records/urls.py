from rest_framework.routers import DefaultRouter
from .views import RecordViewSet

router = DefaultRouter()
router.register("records", RecordViewSet, basename="record")

urlpatterns = router.urls