from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Document)
admin.site.register(Subject)
admin.site.register(School)
admin.site.register(Tags)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Document_file_viewer_background)
