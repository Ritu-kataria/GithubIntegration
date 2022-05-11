from turtle import title
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import UserSerializer
import requests
import json
from .models import Issues, Labels, Assignees

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

issues = Get_Issues_From_Api()

def Add_Issues_Into_DB():
    """
    This function is used to add fetched issues into database
    """
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
    labels = []
    for issue in issues:
        for label in issue['labels']:
            label['reference_id'] = issue['id']
            labels.append(label)

    # Removing duplicate entries
    labels_set = set()
    result = []
    for d in labels:
        h = d.copy()
        h.pop('reference_id')
        h = tuple(h.items())
        if h not in labels_set:
            result.append(d)
            labels_set.add(h)
    return result

def Add_labels_Into_DB():
    """
    This function is used to add labels into database
    """
    labels = Get_Labels_From_Api()
    for label in labels:
        label_data = Labels(
            label_id = label['id'],
            reference_id = label['reference_id'],
            issue = Issues.objects.get(issue_id=label['reference_id']),
            name = label['name'],
            description = label['description'],
        )
        label_data.save()
        all_labels = Issues.objects.all().order_by('-id')
    return all_labels

def Get_Assignees_From_Api():
    """
    This function is used to return assignee fetched from github rest api
    """
    assignees = []
    for issue in issues:
        for assignee in issue['assignees']:
            assignee['reference_id'] = issue['id']
            assignees.append(assignee)
    
    # Removing duplicate entries
    assignee_set = set()
    result = []
    for d in assignees:
        h = d.copy()
        h.pop('reference_id')
        h = tuple(h.items())
        if h not in assignee_set:
            result.append(d)
            assignee_set.add(h)
    return result

def Add_assignees_Into_DB():
    """
    This function is used to add labels into database
    """
    assignees = Get_Assignees_From_Api()
    for assignee in assignees:
        assignee_data = Assignees(
            assignee_id = assignee['id'],
            reference_id = assignee['reference_id'],
            issue = Issues.objects.get(issue_id=assignee['reference_id']),
            name = assignee['login'],
        )
        assignee_data.save()
        all_assignees = Issues.objects.all().order_by('-id')
    return all_assignees