from datetime import timezone
from rest_framework import serializers
from .models import Course, Module, Enrollment, Assignment, Submission
from django.contrib.auth.models import User

# Serializer for User model (for nesting inside other serializers)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer for Course model with nested instructor
class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)  # Nested serializer for instructor

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'created_at']

# Serializer for Module model with nested course data
class ModuleSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)  # Nested serializer for course

    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'content', 'created_at']

# Serializer for Enrollment model with nested user and course data
class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer for user
    course = CourseSerializer(read_only=True)  # Nested serializer for course

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrollment_date']

# Serializer for Assignment model with custom validation for deadline
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'course', 'title', 'description', 'submission_deadline']

    def validate_submission_deadline(self, value):
        # Ensure that the submission deadline is not in the past
        if value < timezone.now():
            raise serializers.ValidationError("Submission deadline cannot be in the past.")
        return value

# Serializer for Submission model with nested assignment data
class SubmissionSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer(read_only=True)  # Nested serializer for assignment

    class Meta:
        model = Submission
        fields = ['id', 'user', 'assignment', 'submission_file', 'grade', 'submission_date']
