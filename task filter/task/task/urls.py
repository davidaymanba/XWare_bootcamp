from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from Blog.views import PostViewSet
from Author.views import AuthorViewSet


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('Blog/',include('Blog.url')),
#     path('Author/',include('Author.url')),

# ]


router = DefaultRouter()
router.register(r'Blog',PostViewSet)
router.register(r'Author',AuthorViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
