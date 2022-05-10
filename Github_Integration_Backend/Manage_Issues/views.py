from turtle import title
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import UserSerializer
import requests
import json
from .models import Issues

# Create your views here.
# Login Api
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Fetching issues from api and storing in db
def Get_Issues_From_Api():
    """
    This function is used to return issues fetched from all pages of github rest api
    """
    per_page = 100
    issues_data = []
    for page in range(1,3):
        url = f"https://api.github.com/search/issues?q=author:davidism%20repo:pallets/click&per_page={per_page}&page={page}"
        response = requests.request("GET", url=url)
        data = json.loads(response.text)
        issues_data.extend(data['items'])

    return issues_data

def Add_Issues_Into_DB():
    """
    This function is used to add fetched issues into database
    """
    issues = Get_Issues_From_Api()
    for issue in issues:
        issue_data = Issues(
            issue_id = issue['id'],
            title = issue['title'],
            number = issue['number'],
            state = issue['state'],
            created_at = issue['created_at'],
            updated_at = issue['updated_at'],
            closed_at = issue['closed_at']
        )
        issue_data.save()
        all_issues = Issues.objects.all().order_by('-id')
    return all_issues

def Get_Labels_From_Api():
    """
    This function is used to return labels fetched from github rest api
    """
    pass
