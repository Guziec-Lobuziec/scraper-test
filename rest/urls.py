from django.urls import path
from rest import views

urlpatterns = [
    path('stats/', views.GloballStats.as_view()),
    path('stats/<str:author>/', views.AuthorStats.as_view()),
    path('authors/', views.Authors.as_view()),
]
