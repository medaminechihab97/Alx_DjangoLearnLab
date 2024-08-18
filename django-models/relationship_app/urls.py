from django.urls import path
from .views import list_books  # Import the list_books function
from . import views

urlpatterns = [
  path('books/', list_books, name='list_books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('register/', views.register_view, name='register'),
]
