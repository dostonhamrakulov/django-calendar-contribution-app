from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('calendar/', views.calendarr, name='blog-calendar'),
    path('contact/', views.contact, name='blog-contact'),
    path('source_code/', views.source_code, name='blog-source_code'),
]
