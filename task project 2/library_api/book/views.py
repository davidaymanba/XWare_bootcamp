from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import books
from .serializers import BooksSerializer
from rest_framework.decorators import api_view
from .serializers import BooksSerializer
from rest_framework import generics
from rest_framework import viewsets




# Create your views here.

class get_post_book (APIView):
    def get (self,request):
        book = books.objects.all()
        serializer = BooksSerializer(book,many=True)
        return Response(serializer.data)


    def post (self,request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(["PUT","GET","PATCH","DELETE"])
def update_book(request,id):
    book = books.objects.filter(id=id).first()
    if request.method == 'GET':
        print("&" * 50)
        print(book)
        serializer = BooksSerializer(book)
        return Response(serializer.data)
    
    if book is None:
        return Response({"details" : "this book is not found"},status=status.HTTP_404_NOT_FOUND)
     
    if request.method == "DELETE":
        book.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    partial = False

    if request.method == "PATCH":
        partial = True
    books_serializers = BooksSerializer(book,request.data,partial=partial)
    books_serializers.is_valid(raise_exception=True)
    books_serializers.save()

    return Response(books_serializers.data,status=status.HTTP_200_OK)



class BookApiView(APIView):

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
    







class BookList(generics.ListAPIView):
    queryset=books.objects.all()
    serializer_class=BooksSerializer


class BookRetrive(generics.RetrieveAPIView):
    queryset=books.objects.all()
    serializer_class=BooksSerializer


class BookCreation(generics.CreateAPIView):
    serializer_class=BooksSerializer


class BookUpdation(generics.UpdateAPIView):
    serializer_class=BooksSerializer


class BookDeletion(generics.DestroyAPIView):
    serializer_class=BooksSerializer



