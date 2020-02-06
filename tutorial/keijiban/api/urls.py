from django.urls import include, path
from rest_framework.routers import DefaultRouter

from keijiban.api import views as qv

router = DefaultRouter()
router.register(r"keijiban", qv.KeijibanViewSet)

urlpatterns = [
    path("", include(router.urls)), 
]