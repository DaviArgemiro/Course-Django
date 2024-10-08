from django.shortcuts import get_object_or_404, render
from catalog.models import Book, BookInstance, Genre, Author, Language
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class AuthorsListView(generic.ListView):
    model = Author

    def get_queryset(self):
        return Author.objects.all()

class BookListView(generic.ListView):
    model = Book
    paginate_by = 1
    
    def get_queryset(self):
        return Book.objects.filter(tittle__icontains='a')[:5]
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'

        return context
    
class BookDetailView(generic.DetailView):
    model = Book

class AuthorsDetailView(generic.DetailView):
    model = Author