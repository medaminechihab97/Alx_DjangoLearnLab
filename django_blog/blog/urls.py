from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('', views.home),
    path('login/', LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    path("home/", views.HomeView.as_view(template_name='blog/registration/login.html'), name='home'),
    path("register/", views.RegisterView.as_view(template_name='blog/registration/login.html'), name='register'),
    path("posts/", views.PostsView.as_view(template_name='blog/registration/login.html'), name='posts'),



]