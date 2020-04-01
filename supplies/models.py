from django.db import models

# Create your models here.


class Supplier(models.Model):
	organization = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	mobile = models.CharField(max_length=11)
	email = models.EmailField(blank=True)

	def __str__(self):
		return self.organization

class Supply(models.Model):
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	REGIONS = (
		("NCR","National Capital Region"),
		("Region I","Ilocos Region"),
		("CAR","Cordillera Administrative Region"),
		("Region II","Cagayan Valley"),
		("Region III","Central Luzon"),
		("Region IV-A","Calabarzon"),
		("Mimaropa","Southwestern Tagalog Region"),
		("Region V","Bicol Region"),
		("Region VI","Western Visayas"),
		("Region VII","Central Visayas"),
		("Region VIII","Eastern Visayas"),
		("Region IX","Zamboanga Peninsula"),
		("Region X","Northern Mindanao"),
		("Region XI","Davao Region"),
		("Region XII","Soccsksargen"),
		("Region XIII","Caraga Region"),
		("BARMM","Bangsamoro Autonomous Region in Muslim Mindanao"),
		)
	region = models.CharField(max_length=47, choices=REGIONS, default=REGIONS[0][0])
	address = models.CharField(max_length=128)
	quantity = models.IntegerField()
	UNITS = (
		("unit","unit"),
		("kg","kilogram"),
		("g","gram"),
		("l","liter"),
		("ml","milliliter"),
		("m","meter"),
		)
	unit = models.CharField(max_length=10, choices=UNITS, default=UNITS[0][0])
	price = models.DecimalField(max_digits=8, decimal_places=2)
	description = models.TextField()
	is_validated = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "supplies"
