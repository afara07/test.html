from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from . models import Register
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields= ('username','email','password')
