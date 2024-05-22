from django.contrib import admin
from .models import Genre,Author,Book,BookInstance,Language


# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 
                    'first_name', 
                    'date_of_birth')
    # 이렇게하면 작가 자세히보기 눌렀을 떄 출생일 사망일 한 줄에 보여짐
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# book상세보기 페이지에서 bookinstance상태보여주기 위한 객체임
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    
    # book 상세보기를 누르면 bookinstance 상세보기를 할 수 잇게 도와준다
    inlines = [BooksInstanceInline]

    
    

@admin.register(BookInstance) #admin.site.register(BookInstance, ..)와같다
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = [
        (None, {'fields' : ('book', 'id')}), # None이라는 부제 아래에 book과  uuid가 보임
        ("Availability", {'fields' : ('status', 'due_back')}) #Avail부제목아래 소그룹으로 status와 due_back        
    ]



admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)