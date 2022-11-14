from django.contrib import admin
from django.urls import path

from ads import views

urlpatterns = [
    path('', views.index),
    path('ads/', views.AdsView.as_view()),
    path('cat/', views.CatView.as_view()),

    path('ads/<int:pk>', views.AdsDetailView.as_view()),
    path('cat/<int:pk>', views.CatDetailView.as_view())
]


