from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.home, name='index'),
    path('home', views.home, name='home'),
    path('index/', views.home, name='home'),

    # Topic List
    path('topics', views.topic_list, name='topic_list'),
    path('topics/<str:category>', views.topic_list, name='topic_list_category'),
    path('topics/detail/<str:topic_name>/', views.topic_detail, name='topic_detail'),
    path('create_animation/<str:topic_name>/', views.create_animation, name='create_animation'),
]
