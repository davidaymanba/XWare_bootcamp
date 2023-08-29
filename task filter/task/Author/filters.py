import django_filters
from .models import Author

class AuthorFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Author
        fields = []



# class AuthorFilter(django_filters.FilterSet):
  
#     Book_Author = django_filters.NumberFilter(field_name='Book_Author__author',lookup_expr='gt')
    
#     class Meta :
#         model = Author
#         fields = []