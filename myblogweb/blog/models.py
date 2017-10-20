from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import markdown
from django.utils.html import strip_tags
#分类
class Category(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
class Test(models.Model):
	name = models.CharField(max_length=50)

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	abstract = models.CharField(max_length=100,blank=True)
	#文章分类
	category = models.ForeignKey(Category)
	#阅读量
	views = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title
	#跳转详情页
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})
	#文章摘要
	def save(self,*args,**kwargs):
		if not self.abstract:
			md = markdown.Markdown(extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
			])
			self.abstract = strip_tags(md.convert(self.content))[:50]
		super(Post,self).save(*args,**kwargs)
	#文章阅读量
	def increase_views(self):
		#浏览量+1
		self.views += 1
		#更新浏览量,覆写save方法
		self.save(update_fields=['views'])



# Create your models here.
