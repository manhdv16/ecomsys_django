from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def user_login(request):
    uname = request.data.get("username")
    password = request.data.get("password")

    if uname and password:
        try:
            user = User.objects.get(username=uname)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=400)

        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid username or password'}, status=400)
    else:
        return Response({'error': 'All fields are mandatory'}, status=400)
