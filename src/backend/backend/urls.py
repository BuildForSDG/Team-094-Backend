"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from login.views import LoginViewSet, LoginListCreate
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 
router.register('login', LoginViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('login.urls')),
    path('v1/', include(router.urls)),
]