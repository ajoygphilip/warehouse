from rest_framework import serializers
from .models import Transaction as Relative_Transaction,Mongo_Transaction

class RelativeTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relative_Transaction
        fields = '__all__'


class MongoTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mongo_Transaction
        fields = '__all__'