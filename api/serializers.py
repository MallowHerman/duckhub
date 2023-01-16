from rest_framework import serializers
from .models import Document, Category, Tags, School, Course, Subject, Document_file_viewer_background
from django.contrib.auth.models import User
from rest_framework.reverse import reverse


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username']

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tags
		fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = '__all__'

class Document_file_viewerSerializer(serializers.ModelSerializer):

	background_file_url = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Document_file_viewer_background
		fields = ['title', 'document_id', 'background_file', 'background_file_url']

	def get_background_file_url(self, obj):
		return f"http://127.0.0.1:8000{obj.background_file.url}"


class DocumentSerializer(serializers.ModelSerializer):
	category = CategorySerializer(Category)
	tags = TagsSerializer(Tags)
	school = SchoolSerializer(School)
	course = CourseSerializer(Course)
	subject = SubjectSerializer(Subject)
	user = UserSerializer(User)
	document_file_viewer = Document_file_viewerSerializer(Document_file_viewer_background, many=True)

	thumbnail_url = serializers.SerializerMethodField('get_thumbnail_url')
	class Meta:
		model = Document
		fields = ['id', 'title', 'slug', 'description', 'tags', 'category', 'document_file', 'thumbnail', 'thumbnail_url', 'document_file_viewer', 'user', 'school', 'course', 'subject', 'downloads', 'likes', 'created', 'updated']

	def get_thumbnail_url(self, obj):
		return f"http://127.0.0.1:8000{obj.thumbnail.url}"