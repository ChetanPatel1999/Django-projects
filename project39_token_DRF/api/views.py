from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    data={
        'username':user.username,
        'email':user.email,
        'is_staff':user.is_staff,
    }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def adminUser(request):
    user = request.user
    data={
        'message':f"Hello {user.username}, you are an admin user.",
    }
    return Response(data)
