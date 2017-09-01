from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm
from django.http import HttpResponse

def post_comment(request,post_pk):
	#获取文章
	post = get_object_or_404(Post,pk=post_pk)
	#如果是POST请求
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect(post)
		else:
			comment_list = post.comment_set.all()
			context = {
				'post':post,
				'form':form,
				'comment_list':comment_list,
				'test':'这是comment的师徒函数'

			}
			return render(request,'blog/detail.html',context=context)
	return redirect(post)


# Create your views here.
