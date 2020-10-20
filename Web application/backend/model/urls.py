from rest_framework import routers
from .viewsets import DengueCaseViewSet, UserViewSet

router = routers.SimpleRouter()
router.register('dengueCases', DengueCaseViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls