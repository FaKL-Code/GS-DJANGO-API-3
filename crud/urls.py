from django.urls import path, include
from .views import DoacaoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('novadoacao', DoacaoViewSet, 'Doacao')

urlpatterns = [
    path('api/', include(router.urls)),
]
