from django.contrib import admin
from .models import Supplier, Supply


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('organization', 'first_name', 'last_name',
                    'mobile', 'email', 'is_verified')


class SuppyAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'name', 'address',
                    'quantity', 'price')


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Supply, SuppyAdmin)
