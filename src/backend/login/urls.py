from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.SocialSerializer.as_view() ),
]