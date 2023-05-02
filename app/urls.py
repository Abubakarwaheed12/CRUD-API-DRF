from django.urls import path
from app.views import todoAPI
urlpatterns = [
    path('', todoAPI )
]
