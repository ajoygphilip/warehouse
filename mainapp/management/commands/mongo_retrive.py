from django.core.management.base import BaseCommand
from pymongo import MongoClient
from mainapp.models import Warehouse, Product,Employee, Transaction, Mongo_Warehouse, Mongo_Product, Mongo_Employee, Mongo_Transaction, Category, Mongo_Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        transaction_data = Mongo_Transaction.objects.filter(employee__rel_id=30)
        for transaction in transaction_data:
            print(f'Transaction of "{transaction.product}" by {transaction.employee} at {transaction.warehouse}')
            

