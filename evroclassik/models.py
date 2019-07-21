from django.db import models


class Catalog(models.Model):
	text = models.CharField(max_length=200, blank=True)
	#image = models.ImageField(upload_to='media')
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text

class Furniture(models.Model):
	name =models.ForeignKey('Catalog', on_delete = models. PROTECT)
	name_furniture = models.CharField(max_length=50, blank=True)
	#image = models.ImageField(upload_to='media')
	price = models.IntegerField()
	text =models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'furnitures'

	def __str__(self):
		return (f'{self.name_furniture}, {self.price} рублей, добавили: ({self.date_added})')