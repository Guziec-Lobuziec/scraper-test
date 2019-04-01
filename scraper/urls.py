from django.urls import path
from scraper import views

urlpatterns = [
    path('stats/', views.GloballStats.as_view()),
]
