from django.urls import path
from animelist import views

urlpatterns = [
    path('join/', views.animelist, name='join'),
]