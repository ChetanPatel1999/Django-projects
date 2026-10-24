from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import blogSerializer
from .models import blog
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def blogList(request):
    if request.method == 'GET':
        blogs = blog.objects.all()
        serializer = blogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = blogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
