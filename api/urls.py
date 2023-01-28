from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
	path('documents/', views.DocumentMixinView.as_view(), name='documents-list'),
	path('documents/<str:pk>/', views.DocumentMixinView.as_view(), name='documents-detail'),
	path('documents/create/', views.DocumentMixinView.as_view(), name='documents-create'),
	path('documents/<str:pk>/update/', views.DocumentMixinView.as_view(), name='documents-update'),
]

