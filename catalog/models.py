import uuid
from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
from django.db.models import (CharField, UniqueConstraint, ManyToManyField,
                              ForeignKey, TextField,DateField)

# 장르

class Genre(models.Model):
    name = CharField(max_length=200, 
                     help_text="장르명",
                     unique=True)
    
    def __str__(self): return self.name
    
    def get_absolute_url(self):
        # 인스턴스 id에 해당하는 url반환
        return reverse('genere_detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            # name 속성 소문자들 유니크해야함
            UniqueConstraint(Lower('name'),
                             # 제약조건명
                             name='genere_name_case_insensitive_unique',
                             violation_error_message='이미존재'
                             ),
        ]

# 책

class Book(models.Model):
    lanauge = ForeignKey('Language', on_delete=models.RESTRICT, null=True)
    title = CharField(max_length=200,
                      help_text='책제목')
    # 한명의 저자는 여러 책을 가질 수 잇다
    # 저자테이블에서 이 저자명은 pk이고 이는 현재 book테이블에서 fk
    # 만약에 author 테이블에서 author가 사라지면 해당책도 삭제되지않도록한다
    # 만약 책도 삭제하고 싶다면 models.CASCADE옵션쓸것
    author = ForeignKey('Author',on_delete=models.RESTRICT, null=True)
    summary = TextField(max_length=1000,
                        help_text="요약")
    # 첫번째인자는 verboseNamed으로 human-readable임
    isbn = CharField('ISBN', unique=True, max_length=13, help_text='고유')
    # 각책의 장르
    # 하나의 장르는 여러개의 책을 가질 수 잇고 
    # 하나의 책은 여러개의 장르를 가질 수 있기 때문에 다대다 관계이다
    genre = ManyToManyField(Genre, help_text="골라라")
    
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse('book-detail',args=[str(self.id)])


# 책 인스턴스 모델
class BookInstance(models.Model):
    book = ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    due_back = DateField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, 
                          default=uuid.uuid4,
                          help_text="기본값")
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )    
    status = CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')
    
    class Meta: # 쿼리 반환시 due_back 기준으로 레코드 정렬
        ordering = ['due_back']
    
    def __str__(self): return f'{self.id} {(self.book.title)}'

class Lanauge(models.Model):
    name = CharField(max_length=200,
                     help_text='언어',
                     unique=True)
    def get_absolute_url(self): return reverse('language-detail', args=[str(self.id)])
    def __str__(self): return self.name
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            ),
        ]
        

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'