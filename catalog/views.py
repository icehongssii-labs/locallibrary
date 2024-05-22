from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
# Create your views here.

def index(request):
    num_instances = BookInstance.objects.all().count()
    num_boooks = Book.objects.all().count()
    
    # 대출가능한 책
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()    
    num_authors = Author.objects.all().count()
    nums_fiction_books = Book.objects.filter(genre__name__icontains='fiction').count()
    context = {
        'num_books':num_boooks,
        'num_instances':num_instances,
        'num_authors':num_authors,
        'num_instances_available':num_instances_available,
        'nums_fiction_books':nums_fiction_books
    }
    # 렌더 파라미터
    # request는 HttpReuqest 객체
    # html
    # html에 렌더링될 변수
    return render(request,'index.html',context)