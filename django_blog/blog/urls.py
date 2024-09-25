from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', blog_views.register, name='register'),
    path('accounts/profile/', blog_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    # path('post/<int:pk>/comments/new//', views.CommentDeleteView.as_view(), name='comment_delete'),
]
