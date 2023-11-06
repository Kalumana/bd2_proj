from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Component, Equipment, ComponentUsage, CustomUser,Types_of_Labor,StockComponents,StockEquipment,Sales,SalesComponent,SalesEquipment,InvoicesSales,InvoicesPurchage

admin.site.register(CustomUser)
admin.site.register(Component)
admin.site.register(Equipment)
admin.site.register(ComponentUsage)
admin.site.register(Types_of_Labor)
admin.site.register(StockComponents)
admin.site.register(StockEquipment)
admin.site.register(Sales)
admin.site.register(SalesComponent)
admin.site.register(SalesEquipment)
admin.site.register(InvoicesSales)
admin.site.register(InvoicesPurchage)









