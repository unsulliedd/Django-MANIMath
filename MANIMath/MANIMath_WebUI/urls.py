from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.home, name='index'),
    path('home', views.home, name='home'),
    path('index/', views.home, name='home'),
]
