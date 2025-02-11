# accounts/utils.py
from django.contrib.auth.models import Permission

def assign_permissions(user):
    if user.role == 'Admin':
        permissions = Permission.objects.all()  # Admin gets all permissions
    elif user.role == 'Instructor':
        permissions = Permission.objects.filter(codename='can_create_course') | Permission.objects.filter(codename='can_view_course')
    elif user.role == 'Student':
        permissions = Permission.objects.filter(codename='can_view_course') | Permission.objects.filter(codename='can_enroll_course')

    # Assign permissions to the user
    user.user_permissions.set(permissions)
    user.save()
