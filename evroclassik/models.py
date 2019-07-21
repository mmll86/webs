from django.db import models


class Catalog(models.Model):
	text = models.CharField(max_length=200, blank=True)
	image = models.ImageField(upload_to='media')
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
