from rest_framework import routers
from profiles.views import UserViewSet



router = routers.SimpleRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls