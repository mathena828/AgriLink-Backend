from django.contrib import admin
from .models import Supplier, Supply

# Register your models here.

class SupplierAdmin(admin.ModelAdmin): 
      list_display = ('organization', 'name', 'mobile','email')

class SuppyAdmin(admin.ModelAdmin):
      list_display = ('supplier', 'name', 'address','quantity','price','is_validated')

admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Supply,SuppyAdmin)