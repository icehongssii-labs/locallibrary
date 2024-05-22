from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
# Create your views here.
from django.views import generic

class BookListView(generic.ListView):
    # model=book으로 generic view가 db에서 book에잇는 레코드 전부가져올것임
    model = Book
    # 그리고 book_list.html에 렌더할것임 ({객체명}_list.html)
    # generic view가 /{어플리케이션이름}/{모델명}_list.html을찾아다닐거임 /{어프리케이션/templates안에서
    # 이런기본설정은 따로 바꿀수있긴함 만약에 특정짓고싶다면 아래와 같이
    
    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.filter(title__icontains='live')[:5]
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # model말고 추가로 더 렌더링하고싶은게잇다면
        context =  super(BookListView, self).get_context_data(**kwargs)
        context['some'] = '추가어쩌구 ㅋ'
        return context


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

class BookDetailView(generic.DetailView):
    model = Book
