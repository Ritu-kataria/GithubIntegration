from django.conf.urls import url
from  ManageIssues import views

urlpatterns = [
    url(r'^', views.getIssues, name='getIssues'),
]