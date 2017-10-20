from django.db import models
from django.core.urlresolvers import reverse
class IMG(models.Model):
	img = models.ImageField(upload_to='uploadimg')
	name = models.CharField(max_length=200,blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = '图片-사진'

# Create your models here.