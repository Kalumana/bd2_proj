from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ManagerProfile, ClientProfile, SupplierProfile


admin.site.register(ManagerProfile)
admin.site.register(SupplierProfile)
admin.site.register(ClientProfile)







