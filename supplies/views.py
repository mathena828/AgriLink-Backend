from django.shortcuts import render
from rest_framework import viewsets 
from .models import Supplier, Supply 
from .serializers import SupplierSerializer, SupplySerializer

# Create your views here.

class SupplierView(viewsets.ModelViewSet):
	serializer_class = SupplierSerializer
	queryset = Supplier.objects.all()

class SupplyView(viewsets.ModelViewSet):
	serializer_class = SupplySerializer
	queryset = Supply.objects.all()       