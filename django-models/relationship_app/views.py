from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library


def list_books(request):
  """Displays a list of all books in the database."""
  books = Book.objects.all()
  context = {'books': books}
  return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'