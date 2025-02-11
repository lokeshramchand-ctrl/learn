from django.contrib import admin
from django.urls import path, include 
from accounts.views import RegisterAPI, LoginAPI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),

]
