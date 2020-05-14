from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.LoginListCreate.as_view() ),
    path('', views.login),
    path('home/', views.home),
    path('logout/', views.logout),
]