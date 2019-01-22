from django.db import models

class Category(models.Model):
	category_name = models.CharField(max_length=128)
	
	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		return self.category_name

class Post(models.Model):
	title = models.CharField(max_length=128)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True, blank=True)
	
	class Meta:
		verbose_name_plural = "posts"

	def __str__(self):
		return self.title