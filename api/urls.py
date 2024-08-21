from django.urls import path
from .views import *
urlpatterns = [
    path('', view=home, name="home"),
    path('add-book', view=book_add, name="book_add"),
    path('edit-book/<int:id>/', view=book_edit, name="book_edit"),
    path('book-delete/<int:id>/', view=book_delete, name="book_delete"),
    
]
