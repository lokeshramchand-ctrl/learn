from rest_framework import serializers
from .models import Course, Module, Enrollment, Assignment, Submission
from django.contrib.auth.models import User

# Serializer for Course model
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'created_at']

# Serializer for Module model
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'content', 'created_at']

# Serializer for Enrollment model
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrollment_date']

# Serializer for Assignment model
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'course', 'title', 'description', 'submission_deadline']

# Serializer for Submission model
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'user', 'assignment', 'submission_file', 'grade', 'submission_date']
