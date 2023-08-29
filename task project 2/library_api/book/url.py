from django.urls import path
from . import views
from .views import get_post_book , update_book
from .views import BookApiView
from .views import BookApiView ,BookCreation,BookDeletion,BookList,BookRetrive,BookUpdation
urlpatterns =[
    path('',get_post_book.as_view(),name="get_post_book"),
    path('<int:id>/',update_book,name="update_book"),
    path('<int:pk>/',BookApiView.as_view()),
    path('','<int:pk>/',BookApiView.as_view()),
    path('','<int:pk>/',BookList.as_view()),
    path('','<int:pk>/',BookRetrive.as_view()),
    path('','<int:pk>/',BookCreation.as_view()),
    path('','<int:pk>/',BookDeletion.as_view()),
    path('','<int:pk>/',BookUpdation.as_view())
]
