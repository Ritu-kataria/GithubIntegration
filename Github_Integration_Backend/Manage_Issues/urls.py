from django import views
from django.db import router
from django.urls import path, include
from Manage_Issues import views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('issues', views.display_issues_with_labels_assignees, name='Issues'),
]