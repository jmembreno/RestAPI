from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import *
from.serializers import *



class BreedList(APIView):
    def get(self,request):
        objs = Breed.objects.all()
        return Response(BreedSerializer(objs,many=True).data)
    def post(self,request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BreedDetail(APIView):
    def get(self,request,id):
        obj = get_object_or_404(Breed,id=id)
        return Response(BreedSerializer(obj).data)
    def put(self,request,id):
        obj = get_object_or_404(Breed,id=id)
        serializer = BreedSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        obj = get_object_or_404(Breed,id=id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DogList(APIView):
    def get(self,request):
        objs = Dog.objects.all()
        return Response(DogSerializer(objs,many=True).data)
    def post(self,request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    def get(self,request,id):
        obj = get_object_or_404(Dog,id=id)
        return Response(DogSerializer(obj).data)
    def put(self,request,id):
        obj = get_object_or_404(Dog,id=id)
        serializer = DogSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        obj = get_object_or_404(Dog,id=id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
