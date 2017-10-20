from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^upload',views.upload_imgs,name='upload_imgs'),
	url(r'^Gallery.*?',views.IndexView.as_view(),name='upload'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)