from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import user_registration

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        try:
            user = User.objects.create_user(username=data['username'], 
            email=data['email'], password=data['password'])

            user_registration.objects.create(
                user=user,
                email=data['email'],
                mobile=data['mobile'],
                password=data['password'],
                address=data['address']
            )
            return Response({'message': 'User registered successfully'}, status=201)
        except KeyError:
            return Response({'error': 'Missing required fields'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
