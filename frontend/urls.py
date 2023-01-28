from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
	path('', views.documentListView, name="document-list"),
	path('upload/', views.documentUploadView, name="document-upload"),
	path('document/<str:pk>', views.documentDetailView, name="document-detail"),
	path('download/', views.download_file, name='download_file')
]
