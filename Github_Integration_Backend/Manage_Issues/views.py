from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import UserSerializer
import requests
import json

# Create your views here.
# Login Api
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Fetching issues from api and storing in db
def Get_Issues_From_Api():
    """
    This function is used to return issues fetched from github rest api
    """
    url = "https://api.github.com/search/issues?q=author:davidism%20repo:pallets/click"
    response = requests.request("GET", url=url)
    data_in_json = json.loads(response.text)
    return data_in_json

def Add_Issues_Into_DB():
    """
    This function is used to add fetched issues into database
    """
    pass