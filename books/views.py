from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    login_url = 'account_login'
    permission_required = 'books.special status'


class SearchListView(ListView):
    # queryset = Book.objects.filter(Q(title__icontains='doom') | Q(title__icontains='aqua'))
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return (queryset := Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)))
        
