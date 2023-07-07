import random
from datetime import datetime, timedelta
from mainapp.models import Warehouse, Category, Product, Employee, Transaction
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.db.models import Count



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        pass
        

    locations = [
        "New York City, NY",
        "Los Angeles, CA",
        "Chicago, IL",
        "Houston, TX",
        "Phoenix, AZ",
        "Philadelphia, PA",
        "San Antonio, TX",
        "San Diego, CA",
        "Dallas, TX",
        "San Jose, CA",
        "Austin, TX",
        "Jacksonville, FL",
        "San Francisco, CA",
        "Indianapolis, IN",
        "Columbus, OH",
        "Fort Worth, TX",
        "Charlotte, NC",
        "Seattle, WA",
        "Denver, CO",
        "Washington, D.C."
    ]

    # Create Warehouses

    # warehouses = []
    # for i in range(10):
    #     location = random.choice(locations)
    #     warehouse = Warehouse(name=f'Warehouse {i+1}', location=location, capacity=random.randint(100, 1000))
    #     warehouse.save()
    #     warehouses.append(warehouse)

    # # Create Categories
    # category_names = [
    # "Electronics",
    # "Clothing",
    # "Home and Kitchen",
    # "Sports and Outdoors",
    # "Beauty and Personal Care",
    # "Automotive",
    # "Books",
    # "Toys and Games",
    # "Health and Household",
    # "Pet Supplies",
    # "Office Products",]

    # for name in category_names:
    #     category = Category(name=name, description=f"Good Quality {name}")
    #     category.save()

    # Create Products
    # for i in range(20):
    #     category=random.choice(list(Category.objects.all()))
    #     product = Product(
    #         category=category,
    #         name=f'{category.name} item {i+1}',
    #         warehouse=random.choice(list(Warehouse.objects.all())),
    #         quantity=random.randint(1, 100),
    #         price=random.uniform(10, 1000)
    #     )
    #     product.save()

    # Create Employees
    names = [
    "John Smith",
    "Emma Johnson",
    "Michael Brown",
    "Sophia Davis",
    "William Wilson",
    "Olivia Taylor",
    "James Clark",
    "Isabella Anderson",
    "Robert Martinez",
    "Ava Thompson"
]
 

    

    # for name in names:
    #     employee = Employee(
    #         name=name,
    #         designation='Warehouse Employee',
    #         warehouse=random.choice(list(Warehouse.objects.all()))
    #     )
    #     employee.save()

    while Transaction.objects.count()<50:
        product =  random.choice(list(Product.objects.all()))
        warehouse= product.warehouse
        employee = random.choice(list(Employee.objects.filter(warehouse=warehouse)))

        print(product,product.warehouse,product.warehouse.id,"\n",
              warehouse,warehouse.id,"\n",
              employee,employee.warehouse.id)
        
        transaction = Transaction(
            product = product,
            warehouse = warehouse,
            employee = employee,
            quantity = random.randint(1, 10)
        )

        transaction.save()


