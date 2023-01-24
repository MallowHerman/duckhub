from django.shortcuts import render, HttpResponse, redirect
import mimetypes
import os
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from api.models import Document, Category, Subject, School, Course, Tags
from .forms import DocumentForm
from django.http import JsonResponse

def documentListView(request):
    return render(request, 'frontend/documentListPage.html')

def documentDetailView(request, pk):
    return render(request, 'frontend/documentDetailPage.html', {'pk': pk})

def documentUploadView(request):
    category = Category.objects.all()
    subjects = Subject.objects.all()
    schools = School.objects.all()
    courses = Course.objects.all()
    tags = Tags.objects.all()
    if request.method == 'POST':
        subject, created = Subject.objects.get_or_create(title=request.POST.get('subject'))
        school, created = School.objects.get_or_create(title=request.POST.get('school'))
        course, created = Course.objects.get_or_create(title=request.POST.get('course'))
        category, created = Category.objects.get_or_create(title=request.POST.get('category'))
        

        save_document = Document.objects.create(
            title = request.POST.get('name'),
            description = request.POST.get('description'), 
            course = course,
            school = school,
            subject = subject,
            category = category,
            document_file = request.FILES['document'],
            user = request.user
        )
        
        print(save_document.document_file.url)
        return redirect('document-list')
    
    context = {
        'category': category,
        'subjects': subjects,
        'schools': schools,
        'courses': courses,
        'tags': tags
    }
    return render(request, 'frontend/documentUploadPage.html', context)



def download_file(request):
    filename = "Trabalho_de_Hemoragia_Obstetrica.pdf"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define the full file path
    filepath = BASE_DIR + '/media/documents/' + filename
    print(filepath)
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
   

    return response
    