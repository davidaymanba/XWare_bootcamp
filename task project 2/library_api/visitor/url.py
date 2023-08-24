from django.urls import path
from . import views
from .views import get_post_visitor, update_visitor


urlpatterns = [

    path('',get_post_visitor.as_view(),name="get_post_visitor"),
    path('/<int:id>/',update_visitor,name="update_visitor")

]