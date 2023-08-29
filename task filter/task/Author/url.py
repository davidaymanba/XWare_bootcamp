from django.urls import path
from . import views
from .views import AuthorViewSet

urlpatterns =[

     path('Author/',AuthorViewSet.as_view(
        {'get':'list',
         'post':'create'})),
    
    path('Author/<int:pk>/',AuthorViewSet.as_view(
        {
         'get':'list' ,
         'post':'create',
         'patch':'partial_update',
         'put' : 'update',
         'delete' : 'destroy',
        })),


]