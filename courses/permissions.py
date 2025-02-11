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
        # Ensure the role check matches the case used in your model ('Instructor' instead of 'instructor')
        return request.user.role == 'Instructor'


class IsStudent(BasePermission):
    """
    Custom permission to allow only students to access certain views.
    """
    def has_permission(self, request, view):
        # Ensure the role check matches the case used in your model ('Student' instead of 'student')
        return request.user.role == 'Student'
