from django.urls import path
from . import views
from .views import get_post_book , update_book

urlpatterns =[
    path('',get_post_book.as_view(),name="get_post_book"),
    path('<int:id>/',update_book,name="update_book")
]
