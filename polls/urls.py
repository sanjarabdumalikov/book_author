from django.urls import path
from .views import (AllCreateBookView,DetailBookView,AuthorView,DetailAuthorView,CreateAuthorView,UpdateAuthorView,
                    DetailUpdateDeleteApiView)
urlpatterns = [
    path('<pk>/', DetailUpdateDeleteApiView.as_view()),
    path('',AllCreateBookView.as_view())
    # path('<int:book_id>',DetailBookView.as_view()),
    # path('create/',CreateBookView.as_view()),
    # path('update/<int:book_id>/',UpdateBookView.as_view())
    # path('delete/<int:book_id>/',DeleteBookView.as_view()),
    # path('detail/<pk>/',DetailBookView.as_view())

#
#     path('author', AuthorView.as_view()),
#     path('author/<int:author_id>', DetailAuthorView.as_view()),
#     path('author/create/', CreateAuthorView.as_view()),
#     path('author/update/<int:author_id>/', UpdateAuthorView.as_view()),
#     path('author/delete/<int:author_id>/', DetailAuthorView.as_view())
]
