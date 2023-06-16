from django.urls import path
from MANIMath_Account import views

urlpatterns = [
    # User Authentication
    path('login',views.login, name='login'),
    path('signin',views.login, name='signin'),
    path('register',views.register, name='register'),
    path('signup',views.register, name='signup'),
    path('logout', views.logout, name='logout'),
]
