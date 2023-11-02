from django.db import models
from django.contrib.auth.models import AbstractUser

class Managers(AbstractUser):
    is_manager = models.BooleanField(default=False)
    # Add other fields for user roles and profile

    def __str__(self):
        return self.username

class Suppliers(AbstractUser):
    is_supplier = models.BooleanField(default=False)
    # Add other fields for user roles and profile

    def __str__(self):
        return self.username

class Clients(AbstractUser):
    is_Client = models.BooleanField(default=False)
    # Add other fields for user roles and profile
    def __str__(self):
        return self.username


class Component(models.Model):
    id_comp = models.BigAutoField(primary_key=True, default=int)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Equipment(models.Model):
    id_equip = models.BigAutoField(primary_key=True, default=int) 
    name = models.CharField(max_length=100)
    description = models.TextField()
    components = models.ManyToManyField(Component, through='ComponentUsage')

class ComponentUsage(models.Model):
    id_comp_usage = models.BigAutoField(primary_key=True, default=int)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class StockComponents(models.Model):
    id_stock_comp = models.BigAutoField(primary_key=True, default=int)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    # Add other fields as needed

class StockEquipment(models.Model):
    id_stock_equip = models.BigAutoField(primary_key=True, default=int)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    # Add other fields as needed

class SalesManager(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other fields as needed

class SalesSupplier(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other fields as needed

class PurchaseSupplier(models.Model):
    suppliers = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other fields as needed

class PurchaseClient(models.Model):
    Client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other fields as needed

class InvoicesSales(models.Model):
    sale_manager = models.ForeignKey(SalesManager, on_delete=models.CASCADE)
    sales_supplier =  models.ForeignKey(SalesSupplier, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed

class InvoicesPurchage(models.Model):
    purchase_client = models.ForeignKey(PurchaseClient, on_delete=models.CASCADE)
    purchase_supplier = models.ForeignKey(PurchaseSupplier, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed
