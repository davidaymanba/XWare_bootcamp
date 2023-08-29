from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import Response
from rest_framework import viewsets ,filters
from .models import Author
from .serializers import AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AuthorFilter


# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter


class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter]
    ordering_fields_= ['id']
    search_fields = ['first_name','last_name']
