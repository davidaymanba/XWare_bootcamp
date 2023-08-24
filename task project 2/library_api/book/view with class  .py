from rest_framework.views import APIView
from .models import books
from .serializers import BooksSerializer
from rest_framework.response import Response
from rest_framework import status


class StudentApiView(APIView):

    def get (self , request):
        booker = books.objects.all().order_by("-id")
        book_serializer = BooksSerializer(booker,many=True)
        return Response (book_serializer.data , status=status.HTTP_200_OK)
    

    def post (self , request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 

        
    def patch (self , requset ,id):
        book = books.objects.filter(id=id).first()
        books_serializers = BooksSerializer(book,requset.data,partial=True)
        books_serializers.is_valid(raise_exception=True)
        books_serializers.save()
        return Response(books_serializers.data,status=status.HTTP_200_OK)
    
    def put (self , requset ,id):
        book = books.objects.filter(id=id).first()
        books_serializers = BooksSerializer(book,requset.data)
        books_serializers.is_valid(raise_exception=True)
        books_serializers.save()
        return Response(books_serializers.data,status=status.HTTP_200_OK)
    
    def delete (self , requset , id ):
        book = books.objects.filter(id=id).first()
        book.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)