from django.shortcuts import render, redirect
from .serializers import DocumentSerializer
from .models import Document
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.db.models import Q 

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
	data = {
		'api-document-list': '/api/documents'
	}
	return Response(data)

@api_view(['GET'])
def getDocumentsList(request):
	if request.method == 'GET':
		query_search = request.GET.get('q')
		if query_search:
			pass
		else:
			query_search = ''

		print(f"Query: {query_search}")

		documents = Document.objects.filter(Q(title__icontains=query_search) |
		Q(description__icontains=query_search) |
		Q(course__title__icontains=query_search) |
		Q(school__title__icontains=query_search) |
		Q(subject__title__icontains=query_search)
		)

		serializer = DocumentSerializer(documents, many=True)
		return Response(serializer.data)

@api_view(['GET', 'PUT', 'Delete'])
def getDocumentDetail(request, document_slug, pk):
	document = Document.objects.get(slug=document_slug, pk=pk)
	if request.method == 'GET':
		serializer = DocumentSerializer(document, many=False)

	if request.method == 'PUT':
		serializer = DocumentSerializer(document, data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			return redirect ('documents-detail', pk=document.id)
		else:
			raise serializer.ValidationError("Something's wrong happended")

	if request.method == 'DELETE':
		document.delete()

	return Response(serializer.data)


@api_view(['POST'])
def uploadDocuments(request):
	if request.method == 'POST':
		data = request.data
		if Document.objects.filter(**data).exists():
			raise serializers.ValidationError('This data already exists')
		else:
			serializer = DocumentSerializer(data=data)
			if serializer.is_valid():
				serializer.save()

				return redirect('documents-list')
			else:
				raise serializers.ValidationError("Something's wrong happended")
	
