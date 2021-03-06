from rest_framework import serializers
from .models import Supplier, Supply


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'organization', 'first_name',
                  'last_name', 'mobile', 'email', 'is_verified','code')


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ('id', 'supplier', 'name', 'address', 'region',
                  'quantity', 'unit', 'price', 'description')
