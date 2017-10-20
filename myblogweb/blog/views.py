from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from django.views.generic import ListView
import markdown
from comments.forms import CommentForm
from django.core.mail import send_mail
from django.http import HttpResponse

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
	post.increase_views()
	post.content = markdown.markdown(post.content,
	                                 extensions=[
		                                 'markdown.extensions.extra',
		                                 'markdown.extensions.codehilite',
		                                 'markdown.extensions.toc',
	                                 ])
	form = CommentForm()
	comment_list = post.comment_set.all()
	context = {
		'post':post,
		'form':form,
		'comment_list':comment_list
	}
	return render(request,'blog/Temp/blog.html',context=context)
#发邮件
def index(request):
	return render(request,'sendemail/send_email.html')

def sendmail(request):
	if request.POST:
		email_title = request.POST.get('Title')
		email_body = request.POST.get('Content')
		email = request.POST.get('ToEmail')
		EMAIL_FROM = '447724352@qq.com'
		send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
		if send_status:
			return HttpResponse('Success')
		else:
			return HttpResponse('Error')
	else:return render(request,'sendemail/send_email.html')
# Create your views here.
