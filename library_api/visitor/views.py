from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import visitor
from .serializers import visitors_serializers
from rest_framework.decorators import api_view


# Create your views here.


class get_post_visitor(APIView):
    def get (self,request):
        visitors = visitor.objects.all()
        serializer = visitors_serializers(visitors,many=True)
        return Response (serializer.data)
    

    def post (self , request):
        serializer = visitors_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(["PUT","PATCH","DELETE"])
def update_visitor (request,id):
    visitors = visitor.objects.filter(id=id).first()
    if visitors is None:
        return Response ({"details" : "this visitor is not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        visitors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    partial = False


    if request.method == "PATCH":
        partial = True
    visitors_serializers = visitors_serializers(visitors,request.data,partial=partial)
    visitors_serializers.is_valid(raise_exception=True)
    visitors_serializers.save()
    return Response(visitors_serializers.data,status=status.HTTP_200_OK)


    