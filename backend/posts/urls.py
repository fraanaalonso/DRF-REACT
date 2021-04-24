from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


app_name='posts'

router = SimpleRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls

