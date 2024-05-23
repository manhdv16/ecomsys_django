from __future__ import unicode_literals
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth.models import User as AuthUser
from .models import Account, Fullname, Address, CustomUser

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    commune = request.data.get('commune')
    district = request.data.get('district')
    province = request.data.get('province')

    if not all([username, email, password, first_name, last_name, commune, district, province]):
        return JsonResponse({'status': 'error', 'message': 'All fields are required'}, status=400)
    try:
        auth_user = AuthUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        account = Account.objects.create(
            email=email,
            password=password
        )
        fullname = Fullname.objects.create(
            first_name=first_name,
            last_name=last_name
        )
        address = Address.objects.create(
            commune=commune,
            distrist=district,
            province=province
        )
        user_info = CustomUser.objects.create(
            user=auth_user,
            account=account,
            fullname=fullname,
            address=address
        )
        return JsonResponse({'status': 'success', 'message': 'User registered successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
