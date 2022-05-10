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
    path('Issues', views.Get_Issues_From_Api, name='Issues'),
]