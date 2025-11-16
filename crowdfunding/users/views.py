from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Parent, Child
from .serializers import ParentSerializer, ChildSerializer

class ParentList(APIView):
    def get(self, request):
        users = Parent.objects.all()
        serializer = ParentSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ParentDetail(APIView):
    def get_object(self, PK):
        try:
            return Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = ParentSerializer(user)
        return Response(serializer.data)

class ChildList(APIView):
    def get(self, request):
        children = Child.objects.all()
        serializer = ChildSerializer(children, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ChildDetail(APIView):
    def get_object(self, pk):
        try:
            return Child.objects.get(pk=pk)
        except Child.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        child = self.get_object(pk)
        serializer = ChildSerializer(child)
        return Response(serializer.data)