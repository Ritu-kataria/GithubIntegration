# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def getIssues(request):
    return HttpResponse("This is a function to fetch issues")
