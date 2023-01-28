from rest_framework import serializers
from .models import Document, Category, Tags, School, Course, Subject
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username']

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'title']

class TagsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tags
		fields = ['id', 'title']

class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = ['id', 'title']

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ['id', 'title']

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ['id', 'title']


class DocumentSerializer(TaggitSerializer, serializers.ModelSerializer):
	category = CategorySerializer(Category)
	school = SchoolSerializer(School)
	course = CourseSerializer(Course)
	subject = SubjectSerializer(Subject)
	user = UserSerializer(User)

	#thumbnail = serializers.SerializerMethodField(read_only=True)
	total_downloads = serializers.SerializerMethodField(read_only=True)
	total_likes = serializers.SerializerMethodField(read_only=True)
	likes = UserSerializer(User, many=True)

	key_words = TagListSerializerField()


	class Meta:
		model = Document
		fields = ['id', 'key_words', 'title', 'slug', 'description', 'category', 'document_file', 'thumbnail', 'user', 'school', 'course', 'subject', 'total_downloads', 'likes', 'total_likes', 'created', 'updated']

	# def get_thumbnail(self, obj):
	# 	return obj.thumbnail.url

	def get_total_downloads(self, obj):
		return {obj.get_total_downloads()}
	
	def get_total_likes(self, obj):
		return {obj.get_total_likes()}
