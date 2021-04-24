from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


app_name='accounts'

router = SimpleRouter()

router.register('accounts', AccountViewSet, basename='accounts')

urlpatterns = router.urls

