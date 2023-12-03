from django import forms
from .models import Manager, Client, Supplier, Component, Labor, Equipment, StockComponents, StockEquipments, PurshaseEquipment

class ManagerForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    # Adicione os demais campos conforme necessário

class ClientForm(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()
    nif = forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length=256)
    postal_code = forms.CharField(max_length=10)
    create_at = forms.DateTimeField()

class SupplierForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()
    nif = forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea)

class ComponentForm(forms.Form): 
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)  
    price = forms.DecimalField(decimal_places=2, max_digits=6)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())

class LaborForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(decimal_places=2, max_digits=6)

class EquipmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(decimal_places=2, max_digits=6)
    type_equip = forms.CharField(max_length=100)
    type_labor = forms.ModelChoiceField(queryset=Labor.objects.all())
    quantity = forms.IntegerField()
    state = forms.ChoiceField(choices=Equipment.STATUS)

class ComponentUsageForm(forms.Form):
    component = forms.ModelChoiceField(queryset=Component.objects.all())
    equipment = forms.ModelChoiceField(queryset=Equipment.objects.all())

class StockComponentsForm(forms.Form):
    component = forms.ModelChoiceField(queryset=Component.objects.all())
    quantity = forms.IntegerField()

class StockEquipmentsForm(forms.Form):
    equipment = forms.ModelChoiceField(queryset=Equipment.objects.all())
    quantity = forms.IntegerField()

class PurchaseEquipmentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Client.objects.all())
    equipment = forms.ModelChoiceField(queryset=Equipment.objects.all())
    date = forms.DateField()