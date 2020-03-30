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
	address = models.CharField(max_length=128)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	description = models.TextField()
	is_validated = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "supplies"
