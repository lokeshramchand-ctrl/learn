from rest_framework.permissions import BasePermission

class IsAdminOrInstructor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['Admin', 'Instructor']
        
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Student'