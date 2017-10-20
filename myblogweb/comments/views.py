from django.shortcuts import render,get_object_or_404,redirect
#从blog模型中导入Post--联系文章
from blog.models import Post
#从自身模型中导入Comment--保存评论
from .models import Comment
#从表单模型中导入CommentForm--设置表单
from .forms import CommentForm

def post_comment(request,post_pk):
	#接收请求和参数
	#从Post表里按post_pk获得文章
	post = get_object_or_404(Post,pk=post_pk)
	#如果是post方法,需要处理表单数据（if this is a POST request we need to process the form data）
	if request.method == 'POST':
		#根据请求数据实例化表单（create a form instance and populate it with data form the request）
		form = CommentForm(request.POST)
		#如果表单数据合法
		if form.is_valid():
			#保存表单数据到comment,commit:仅仅实例化，并不保存到数据库
			comment = form.save(commit=False)
			#关联评论和文章
			comment.post = post
			#保存评论
			comment.save()
			#重定向到post的详情页
			return redirect(post)
		else:
			comment_list = post.comment_set.all()
			context = {
				'post':post,
				'form':form,
				'comment_list':comment_list
			}
			return render(request,'blog/Temp/blog.html',context=context)
		return redirect(post)


