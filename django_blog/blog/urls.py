from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', blog_views.register, name='register'),
    path('profile/', blog_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]