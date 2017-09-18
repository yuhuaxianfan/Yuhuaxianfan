from ..models import Post,Category
from django import template
from django.db.models.aggregates import Count
#注册
register = template.Library()
#获得最新文章列表
@register.simple_tag
def get_recent_posts(num=4):
	return Post.objects.all().order_by('created_time')[:num]
#分类标签
@register.simple_tag
def get_categories():
	return Category.objects.annotate(num_posts = Count('post')).filter(num_posts__gt=0)