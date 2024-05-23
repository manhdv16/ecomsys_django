from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.contrib.auth.models import User as AuthUser
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return JsonResponse({'status': 'error', 'message': 'Username and password are required'}, 
        status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key, 'status': 'success',
         'message': 'User logged in successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid username or password'}, status=400)
