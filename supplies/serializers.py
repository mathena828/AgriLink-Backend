from rest_framework import serializers
from .models import Supplier, Supply

class SupplierSerializer(serializers.ModelSerializer):
	class Meta:
		model = Supplier
		fields = ('id','organization','name','mobile','email')

class SupplySerializer(serializers.ModelSerializer):
	class Meta:
		model = Supply
		fields = ('id','supplier','name','address','region','quantity','unit','price','description','is_validated')