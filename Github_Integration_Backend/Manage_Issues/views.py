from ast import Return
from turtle import title
from urllib import response
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import UserSerializer, IssuesSerializer, LabelsSerializer, AssigneesSerializer
import requests
import json
from .models import Issues, Labels, Assignees
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# Login Api
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Fetching issues from api and storing in db
def get_issues_from_api():
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

issues_data = get_issues_from_api()

def add_issues_into_db():
    """
    This function is used to add fetched issues into database
    """
    for issue in issues_data:
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

def get_labels_from_api():
    """
    This function is used to return labels fetched from github rest api
    """
    labels = []
    for issue in issues_data:
        for label in issue['labels']:
            label['reference_id'] = issue['id']
            labels.append(label)

    # Removing duplicate entries
    labels_set = set()
    result = []
    for label in labels:
        temp_label = label.copy()
        temp_label.pop('reference_id')
        temp_label = tuple(temp_label.items())
        if temp_label not in labels_set:
            result.append(label)
            labels_set.add(temp_label)
    return result

def add_labels_into_db():
    """
    This function is used to add labels into database
    """
    labels = get_labels_from_api()
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

def get_assignees_from_api():
    """
    This function is used to return assignee fetched from github rest api
    """
    assignees = []
    for issue in issues_data:
        for assignee in issue['assignees']:
            assignee['reference_id'] = issue['id']
            assignees.append(assignee)
    
    # Removing duplicate entries
    assignee_set = set()
    result = []
    for assignee in assignees:
        temp_assignee = assignee.copy()
        temp_assignee.pop('reference_id')
        temp_assignee = tuple(temp_assignee.items())
        if temp_assignee not in assignee_set:
            result.append(assignee)
            assignee_set.add(temp_assignee)
    return result

def add_assignees_into_db():
    """
    This function is used to add labels into database
    """
    assignees = get_assignees_from_api()
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

# Api for returning response of issues, labels and assignees
@api_view(['GET'])
def display_issues_with_labels_assignees(request):
    issues_object = Issues.objects.all()
    labels_object = Labels.objects.all()
    assignees_object = Assignees.objects.all()
    issues_serializer_object = IssuesSerializer(issues_object, many=True)
    labels_serializer_object = LabelsSerializer(labels_object, many=True)
    assignees_serializer_object = AssigneesSerializer(assignees_object, many=True)
    return Response({'issues': issues_serializer_object.data, 'labels': labels_serializer_object.data, 'assignees': assignees_serializer_object.data, 'status': status.HTTP_200_OK})