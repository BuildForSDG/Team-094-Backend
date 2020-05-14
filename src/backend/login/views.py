from django.shortcuts import render
from .models import Login
from .serializers import LoginSerializer
from rest_framework import generics
from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
class LoginListCreate(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')