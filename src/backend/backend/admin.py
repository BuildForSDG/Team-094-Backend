from django.contrib import admin
from django.login.models import Login 
from django.login.admin import LoginAdmin 
class AdminSite(admin.AdminSite): 
    pass 
site = AdminSite()  
site.register(Login, LoginAdmin)