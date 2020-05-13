from django.shortcuts import render
from .models import Login
from .serializers import LoginSerializer
from rest_framework import generics

# Create your views here.
class LoginListCreate(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

