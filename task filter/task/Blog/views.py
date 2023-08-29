from django.shortcuts import render
from rest_framework.views import Response
from rest_framework import viewsets
from .models import Post
from .serializers import PostsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter



# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter