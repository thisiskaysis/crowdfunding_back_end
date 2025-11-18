from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Child
from .serializers import CustomUserSerializer, ChildSerializer, CustomUserCreateSerializer

# Create a new user
class CustomUserRegister(APIView):
    def post(self, request, format=None):
        serializer = CustomUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Retrieve or update user details
class CustomUserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None): #PUT/POST/PATCH????
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# List all children of a user
class ChildList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        children = Child.objects.filter(parent=request.user)
        serializer = ChildSerializer(children, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(parent=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a specific child
class ChildDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Child.objects.get(pk=pk)
        except Child.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        child = self.get_object(pk)
        serializer = ChildSerializer(child)
        return Response(serializer.data)

    def put(self, request, pk, format=None): #PUT/POST/PATCH???
        child = self.get_object(pk)
        serializer = ChildSerializer(child, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        child = self.get_object(pk)
        child.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)