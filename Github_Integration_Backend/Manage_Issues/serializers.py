from urllib import response
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Issues, Labels, Assignees

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user

class IssuesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Issues
        fields = '__all__'

class LabelsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Labels
        fields = ['id', 'label_id', 'reference_id', 'name', 'description']
        
class AssigneesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assignees
        fields = ['id', 'assignee_id', 'reference_id', 'name']