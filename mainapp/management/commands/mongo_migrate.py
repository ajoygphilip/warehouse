from django.core.management.base import BaseCommand
from pymongo import MongoClient
from mainapp.models import Warehouse, Product,Employee, Transaction, Mongo_Warehouse, Mongo_Product, Mongo_Employee, Mongo_Transaction, Category, Mongo_Category
from django.db import DatabaseError
from djongo.exceptions import SQLDecodeError
from bson.decimal128 import Decimal128

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        transactions_to_migrate=Transaction.objects.filter(employee__id=29)
        print(f"total {transactions_to_migrate.count()} transactions to migrate")
        for transaction in transactions_to_migrate:
            print(transaction.id,transaction.employee, transaction.warehouse,"\n",
                  transaction.employee,transaction.employee.warehouse, "\n",
                  transaction.product, transaction.product.warehouse,"\n")

            warehouse = transaction.warehouse
            product = transaction.product
            employee = transaction.employee
            
            new_mongo_warehouse, created =  Mongo_Warehouse.objects.get_or_create(rel_id=warehouse.id,
                                                      location=warehouse.location,
                                                      name= warehouse.name,
                                                      capacity=warehouse.capacity)

            
            new_mongo_category, created = Mongo_Category.objects.get_or_create(rel_id = product.category.id,
                                                name = product.category.name,
                                                description = product.category.description)            

            new_mongo_product,created = Mongo_Product.objects.get_or_create(rel_id = product.id,
                                                    name = product.name,
                                                    category = new_mongo_category,
                                                    warehouse= new_mongo_warehouse,
                                                    quantity = product.quantity,
                                                        )
            #todo find why decimal fields cannot be direclty entered through create
            new_mongo_product.price= product.price
            new_mongo_product.save(update_fields=["price"])
            
            
            new_mongo_employee,created = Mongo_Employee.objects.get_or_create(rel_id=employee.id,
                                        name=employee.name,
                                        designation= employee.designation,
                                        warehouse=new_mongo_warehouse
                )
            new_mongo_transaction = Mongo_Transaction.objects.create(rel_id=transaction.id,
                                                                     product=new_mongo_product,
                                                                     warehouse= new_mongo_warehouse,
                                                                     employee=new_mongo_employee,
                                                                     quantity =transaction.quantity)
            
            
            
            

