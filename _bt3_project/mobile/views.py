from django.shortcuts import render
from .models import Mobile
from rest_framework import viewsets
from .serializers import MobileSerializer

def mobiles(request):
    mobiles = Mobile.objects.all()
    context = {'mobiles': mobiles}
    return render(request, 'mobile_list.html', context)

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
