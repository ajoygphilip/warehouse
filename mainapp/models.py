from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,related_name="employees")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Transaction {self.id}"



    
  
'''Mongo Models'''


class Mongo_Warehouse(models.Model):
    rel_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

class Mongo_Category(models.Model):
    rel_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Mongo_Product(models.Model):
    rel_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Mongo_Category, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Mongo_Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return self.name
    

class Mongo_Employee(models.Model):
    rel_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Mongo_Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Mongo_Transaction(models.Model):
    rel_id = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Mongo_Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Mongo_Warehouse, on_delete=models.CASCADE)
    employee = models.ForeignKey(Mongo_Employee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Transaction {self.id}"
    