from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

    
class Manager(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128) 
    def __str__(self):
        return self.username

class Client(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=True, default=int)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    nif = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=10)
    create_at = models.DateTimeField()


class Supplier(models.Model):
   id = models.BigAutoField(primary_key=True, serialize=True, default=int)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   email = models.EmailField()
   phone = models.IntegerField()
   nif = models.IntegerField()
   address = models.TextField()

class Component(models.Model): 
    id_comp = models.BigAutoField(primary_key=True,serialize = True, default=int)
    name = models.CharField(max_length=100)
    description = models.TextField()  
    price = models.DecimalField(decimal_places=2, max_digits=6)
    images = ArrayField(models.CharField(max_length=100, blank=True), default=list)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Labor(models.Model):
    id_labor = models.BigAutoField(primary_key=True,serialize = True, default=int)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)

   
class Equipment(models.Model):
   ANALYSING = 'analysing'
   PRODUCING = 'producing'
   PRODUCED = 'produced'
   DELIVERY = 'delivery'
   STATUS = [
       (ANALYSING, ('Em analise')),
       (PRODUCING, ('A produzir')),
       (PRODUCED , ('Produzido')),
       (DELIVERY , ('Entregue')),
   ]
   id_equip = models.BigAutoField(primary_key=True, serialize = True, default=int) 
   name = models.CharField(max_length=100)
   description = models.TextField()
   price = models.DecimalField(decimal_places=2, max_digits=6)
   components = models.ManyToManyField(Component, through='ComponentUsage')
   created_at = models.DateTimeField(auto_now_add=True)
   type_equip = models.CharField(max_length=100)
   images = ArrayField(models.ImageField())
   type_labor = models.ForeignKey(Labor,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField()
   state = models.CharField(
        choices= STATUS,
        max_length=9,
        default='ANALYSING',
        )
    

class ComponentUsage(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
   

class StockComponents(models.Model):
    id_stock_comp = models.BigAutoField(primary_key=True,serialize = True, default=int)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    # Add other fields as needed

class StockEquipments(models.Model):
    id_stock_equip = models.BigAutoField(primary_key=True, serialize = True,default=int)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    # Add other fields as needed

class PurshaseEquipment(models.Model):
    id_purchase = models.BigAutoField(primary_key=True, serialize = True, default=int)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)