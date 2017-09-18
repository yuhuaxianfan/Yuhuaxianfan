from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from django.views.generic import ListView
import markdown
# def index(request):
# 	post_list = Post.objects.all()
# 	return render(request,'blog/Temp/index.html',{'post_list':post_list})
#类视图
class IndexView(ListView):
	model = Post
	template_name = 'blog/Temp/post.html'
	context_object_name = 'post_list'
	paginate_by = 3
def category(request,pk):
	cate = get_object_or_404(Category,pk=pk)
	post_list = Post.objects.filter(category=cate).order_by('-id')
	return render(request,'blog/Temp/post.html',{'post_list':post_list})

def detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.content = markdown.markdown(post.content,
	                                 extensions=[
		                                 'markdown.extensions.extra',
		                                 'markdown.extensions.codehilite',
		                                 'markdown.extensions.toc',
	                                 ])
	return render(request,'blog/Temp/blog.html',context={'post':post})

# Create your views here.
