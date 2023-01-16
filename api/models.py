from django.db import models
import uuid
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=100, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Tags(models.Model):
	title = models.CharField(max_length=100, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class School(models.Model):
	title = models.CharField(max_length=100, null=True)
	slug = models.SlugField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super().save(*args, **kwargs)


class Course(models.Model):
	title = models.CharField(max_length=100, null=True)
	slug = models.SlugField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super().save(*args, **kwargs)


class Subject(models.Model):
	title = models.CharField(max_length=100, null=True)
	slug = models.SlugField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

class Document_file_viewer_background(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	document_id = models.ForeignKey('Document', on_delete=models.CASCADE, null=True)
	background_file = models.FileField(upload_to='documents/background_files/')

	def __str__(self):
		return self.title



class Document(models.Model):
	id = models.UUIDField(primary_key = True, unique= True, default = uuid.uuid4, editable = False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=300)
	slug = models.SlugField(null=True, blank=True)
	description = models.TextField(null=True)
	thumbnail = models.ImageField(upload_to='thumbnail/')
	document_file = models.FileField(upload_to='documents/')
	document_file_viewer = models.ManyToManyField(Document_file_viewer_background, related_name="document_file_viewer")
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	tags = models.ManyToManyField(Tags, related_name="tags")
	school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
	course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
	likes = models.ManyToManyField(User, related_name="document_likes")
	downloads  = models.ManyToManyField(User, related_name="document_downloads")

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created', '-updated']

	def __str__(self):
		return self.title


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super().save(*args, **kwargs)




