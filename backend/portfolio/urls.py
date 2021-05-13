

from .views import *
from rest_framework.routers import SimpleRouter

app_name='portfolio'

router = SimpleRouter()

router.register('skills', SkillViewSet, basename='skills')
router.register('projects', ProjectViewSet, basename='projects')


urlpatterns = router.urls
