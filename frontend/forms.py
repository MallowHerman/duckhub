from django import forms
from api.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'document_file', 'category', 'subject', 'school', 'course', 'description', 'key_words']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'document_file': forms.FileInput(attrs={'class': 'form-control'}),
            'key_words': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'row': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-control', 'list': 'datalistSubject'}),
            'school': forms.Select(attrs={'class': 'form-control', 'list': 'datalistSchool'}),
            'course': forms.Select(attrs={'class': 'form-control', 'list': 'datalistCourse'}),
        }