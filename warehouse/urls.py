from django.urls import path, include
from rest_framework import routers
from mainapp.views import RelativeTransactionViewSet,MongoTransactionViewSet

router = routers.DefaultRouter()
router.register(r'transactions', RelativeTransactionViewSet)
router.register(r'mongotransactions', MongoTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
