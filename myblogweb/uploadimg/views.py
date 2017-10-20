from django.shortcuts import render
from .models import IMG
from django.views.generic import ListView

class IndexView(ListView):
	model = IMG
	template_name = 'blog/Temp/Gallery.html'
	context_object_name = 'imgs'
	paginate_by = 12
def upload_imgs(request):
	if request.method == 'POST':
		new_img = IMG(img=request.FILES.get('img'),name=request.FILES.get('img').name)
		new_img.save()
	return render(request,'uploadimg/upload.html')
# Create your views here.
