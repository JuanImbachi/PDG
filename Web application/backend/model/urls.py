from rest_framework import routers
from .viewsets import DengueCaseViewSet

router = routers.SimpleRouter()
router.register('dengueCases', DengueCaseViewSet)

urlpatterns = router.urls