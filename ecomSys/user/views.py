from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, password=password,
                                        email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        # return JsonResponse({'message': 'User registered successfully'})
    else:
        return JsonResponse({'error': 'Username already exists'}, status=400)

@csrf_exempt
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'message': 'Login successful'})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
