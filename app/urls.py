from django.urls import path
from app.views import  TodoAPI
urlpatterns = [
    path('', TodoAPI.as_view() )
]
