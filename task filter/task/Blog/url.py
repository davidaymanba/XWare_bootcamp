from django.urls import path
from . import views
from .views import PostViewSet

urlpatterns =[

     path('post/',PostViewSet.as_view(
        {'get':'list',
         'post':'create'})),
    
    path('post/<int:pk>/',PostViewSet.as_view(
        {
         'get':'list' ,
         'post':'create',
         'patch':'partial_update',
         'put' : 'update',
         'delete' : 'destroy',
        })),


]

