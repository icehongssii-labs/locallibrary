from django.urls import path
from . import views

urlpatterns = [
    # 저기에 있는 name 파라미터로
    # <html><a href="{% url 'index' %}">Home</a>.</html>
    # 이름식으로 url이름을 지어줄수잇음
    # 그냥 하드코딩헤서 /catalog/index 이런식으로 할수잇지만
path('', views.index, name='index'),
# 이번에는 view를 클래스형식으로 가져올것임
path('books/', views.BookListView.as_view(), name='books'),

]
