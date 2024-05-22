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

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    

@admin.register(BookInstance) #admin.site.register(BookInstance, ..)와같다
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')



admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)