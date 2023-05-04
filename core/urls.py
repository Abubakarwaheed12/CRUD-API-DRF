from django.contrib import admin
from django.urls import path , include 
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapi/', TodoAPI.as_view() ),
    path('todoapi/<int:pk>/', TodoAPI.as_view() ),
]
