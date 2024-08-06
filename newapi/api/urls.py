
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('v1/foods/', views.GetFoodInfoView.as_view())
]
