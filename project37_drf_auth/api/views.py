from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def public(request): 
    data = {
        'message': 'This is a public api.',
        "status": 'success',
        'access': 'anyone can access this api without authentication.',
    }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private(request):
    data = {
        'message': 'This is a private api.',
        "status": 'success',
        'access': 'only authenticated users can access this api.',
    }
    return Response(data)