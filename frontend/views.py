from django.shortcuts import render, HttpResponse, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from api.models import Document, Category, Subject, School, Course
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

def documentListView(request):
    if 'query_search' in request.GET:
        query_search = request.GET.get('query_search')

        multiple_q = Q(Q(title__icontains=query_search) | 
            Q(description__icontains=query_search) | 
            Q(school__title__icontains=query_search) | 
            Q(subject__title__icontains=query_search) | 
            Q(course__title__icontains=query_search)
        )
        
        documents = Document.objects.filter(multiple_q)
        print(documents.first().key_words.all())
    else:
        documents = Document.objects.all()


    page = Paginator(documents, 5)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page
    }
    return render(request, 'frontend/documentListPage.html', context)

def documentDetailView(request, pk):
    return render(request, 'frontend/documentDetailPage.html', {'pk': pk})

@login_required(login_url='login')
def documentUploadView(request):
    category = Category.objects.all()
    subjects = Subject.objects.all()
    schools = School.objects.all()
    courses = Course.objects.all()
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            print('ok')
            return redirect('frontend:document-list')   

    form = DocumentForm()
    
    context = {
        'category': category,
        'subjects': subjects,
        'schools': schools,
        'courses': courses,
        'form': form
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
    