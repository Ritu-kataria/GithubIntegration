from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('This is login page')

def getIssues(request):
    return HttpResponse('This is getIssues page')
