from django.urls import path
from . import views

urlpatterns = [
	path('documents/', views.getDocumentsList, name='documents-list'),
	path('documents/<slug:document_slug>/<str:pk>/', views.getDocumentDetail, name='documents-detail'),
	path('documents/upload/', views.uploadDocuments, name='documents-upload'),
]

