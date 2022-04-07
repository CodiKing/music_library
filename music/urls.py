from django.urls import path
from . import views

urlpatterns=[
    path('', views.song_list),
    path('music int<pk>/', views.song_detail)
]