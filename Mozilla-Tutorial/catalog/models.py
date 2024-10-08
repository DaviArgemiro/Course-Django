import uuid
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book a genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(help_text='Enter the name of language of book', max_length=200)
    
class Book(models.Model):
    tittle = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISNB', max_length=13, help_text='13 Character <a href="https:////www.isbn-international.org/content/what-isbn">ISNB number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a Genre for this book')

    def __str__(self):
        return self.tittle
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('m', 'Maintence'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.tittle})'
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        print(self.id)
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'