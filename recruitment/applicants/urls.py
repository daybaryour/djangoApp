#use router from rest framework as against using paths
from rest_framework import routers
from .api import ApplicantViewSet

router = routers.DefaultRouter()

#register all url endpoints
router.register('api/applicants', ApplicantViewSet, 'applicants')

#set url patterns into router.urls
urlpatterns = router.urls
