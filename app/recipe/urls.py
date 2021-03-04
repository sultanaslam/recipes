from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tags', views.TagViewSet, basename='tags')

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
