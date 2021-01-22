from django.urls import path
from list import views

urlpatterns = [
    path('main/', views.list, name='main'),
]