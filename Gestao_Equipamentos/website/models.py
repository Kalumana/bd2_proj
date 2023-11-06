from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPES = [
        ('manager', 'Manager'),
        ('supplier', 'Supplier'),
        ('client', 'Client'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    # Add any additional fields specific to user profiles

    def __str__(self):
        return f'{self.user.username} ({self.user_type})'


class Component(models.Model):
    id_comp = models.BigAutoField(primary_key=True, default=int)
    name = models.CharField(max_length=100)
    description = models.TextField()  
    price = models.DecimalField(decimal_places=2, max_digits=6)

class Types_of_Labor(models.Model):
    id_labor = models.BigAutoField(primary_key=True, default=int)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)

   
class Equipment(models.Model):
   ANALYSING = 'analysing'
   PRODUCING = 'producing'
   PRODUCED = 'produced'
   STATUS = [
       (ANALYSING, ('Analisando equipamento')),
       (PRODUCING, ('produxindo equipamento')),
       (PRODUCED , ('euipamento produzido')),
   ]
   id_equip = models.BigAutoField(primary_key=True, default=int) 
   name = models.CharField(max_length=100)
   description = models.TextField()
   price = models.DecimalField(decimal_places=2, max_digits=6)
   components = models.ManyToManyField(Component, through='ComponentUsage')
   type_equip = models.CharField(max_length=100)
   type_labor = models.ForeignKey(Types_of_Labor,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField()
   state = models.CharField(
        choices= STATUS,
        max_length=4,
        default='ANALYSING',
        )

class ComponentUsage(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
   

class StockComponents(models.Model):
    id_stock_comp = models.BigAutoField(primary_key=True, default=int)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # Add other fields as needed

class StockEquipment(models.Model):
    id_stock_equip = models.BigAutoField(primary_key=True, default=int)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    # Add other fields as needed

class Sales(models.Model):
    manager = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Suppliers = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Component = models.ManyToManyField(Component, through='SalesComponent')
    Equipment = models.ManyToManyField(Equipment, through='SalesEquipment')
    date = models.DateField()
    # Add other fields as needed

class SalesComponent(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)

class SalesEquipment(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)

class Purchases(models.Model):
    id_purchase = models.BigAutoField(primary_key=True, default=int)
    manager = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Component = models.ManyToManyField(Component, through='PurshaseComponent')
    Equipment = models.ManyToManyField(Equipment, through='PurshaseEquipment')
    date = models.DateField()
    # Add other fields as needed

class PurshaseComponent(models.Model):
    purchase = models.ForeignKey(Purchases, on_delete=models.CASCADE)

class PurshaseEquipment(models.Model):
    purchase = models.ForeignKey(Purchases, on_delete=models.CASCADE)

class InvoicesSales(models.Model):
    sale = models.OneToOneField(Sales, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Add other fields as needed

class InvoicesPurchage(models.Model):
    purchase = models.OneToOneField(Purchases, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Add other fields as needed
