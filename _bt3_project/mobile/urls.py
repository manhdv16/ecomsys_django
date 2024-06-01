from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'mobiles', views.MobileViewSet)

urlpatterns = [
    path('mobile/list/', views.mobiles, name='mobile_list'),
    path('', include(router.urls)),
]
