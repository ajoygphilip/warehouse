from django.shortcuts import render
from .models import Transaction as Relative_Transaction,Mongo_Transaction
from rest_framework.viewsets import ModelViewSet
from .serializers import RelativeTransactionSerializer,MongoTransactionSerializer
# Create your views here.


class RelativeTransactionViewSet(ModelViewSet):
    queryset = Relative_Transaction.objects.all()
    serializer_class = RelativeTransactionSerializer


class MongoTransactionViewSet(ModelViewSet):
    queryset = Mongo_Transaction.objects.all()
    serializer_class = MongoTransactionSerializer
