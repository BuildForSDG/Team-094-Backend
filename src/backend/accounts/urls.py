from django.urls import path
from .views import (SocialSerializer)

urlpatterns = [
    path('oauth/login/', SocialSerializer.as_view())
]