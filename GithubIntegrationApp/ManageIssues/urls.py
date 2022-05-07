from django import views
from django.urls import path
from ManageIssues import views

urlpatterns = [
    path('', views.login, name='login'),
    path('Issues', views.getIssues, name='Issues'),
]