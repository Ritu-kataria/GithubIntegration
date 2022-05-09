from django import views
from django.db import router
from django.urls import path, include
from ManageIssues import views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('Issues', views.getIssues, name='Issues'),
]