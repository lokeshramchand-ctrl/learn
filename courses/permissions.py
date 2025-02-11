# course/permissions.py
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Custom permission to allow only admins to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_staff  # Assuming 'is_staff' is used for admin users


class IsInstructor(BasePermission):
    """
    Custom permission to allow only instructors to access certain views.
    """
    def has_permission(self, request, view):
        # Check if the user has 'instructor' role (adjust based on your model)
        return request.user.role == 'instructor'


class IsStudent(BasePermission):
    """
    Custom permission to allow only students to access certain views.
    """
    def has_permission(self, request, view):
        # Check if the user has 'student' role (adjust based on your model)
        return request.user.role == 'student'
