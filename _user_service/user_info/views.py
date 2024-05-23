from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user_model.models import CustomUser

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    auth_user = request.user
    try:
        custom_user = CustomUser.objects.get(user=auth_user)
        account = custom_user.account
        fullname = custom_user.fullname
        address = custom_user.address
        user_data = {
            'id': auth_user.id,
            'username': auth_user.username,
            'email': auth_user.email,
            'first_name': fullname.first_name,
            'last_name': fullname.last_name,
            'commune': address.commune,
            'district': address.distrist, 
            'province': address.province,
        }
        return Response({'status': 'success', 'user': user_data})
    except CustomUser.DoesNotExist:
        return Response({'status': 'error', 'message': 'User details not found'}, status=404)
