from django.db import models

# Create your models here.
class Supplier(models.Model):
	name = models.CharField(max_length=300)
	city = models.CharField(max_length=300)
	country = models.CharField(max_length=300)
	created_at = models.DateTimeField(blank=True, null=True)
	objects = models.Manager()
	def getName(self):
		return self.name
	def __str__(self):
		return  self.name + '- ' + self.city + ', ' + self.country + 'created at:' + self.created_at
        

class WaterBottle(models.Model):
	SKU = models.CharField(max_length=3)
	brand = models.CharField(max_length=300)
	cost = models.DecimalField
	size = models.CharField(max_length=300)
	mouth = models.CharField(max_length=300)
	color = models.CharField(max_length=300)
	supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	current_quantity = models.IntegerField
	objects = models.Manager()
