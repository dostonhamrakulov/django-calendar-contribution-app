from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('calendar/', views.calendarr, name='blog-calendar'),
    path('calendar/', views.calendarr, name='blog-contact'),
    path('calendar/', views.calendarr, name='blog-source_code'),
]
