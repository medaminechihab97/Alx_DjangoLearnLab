from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('', views.home),
    path('signup', views.SignUpView.as_view()),
    path('login/', LoginView.as_view(template_name='blog/registration/login.html'), name='login'),


]