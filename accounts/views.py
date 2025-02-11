from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth.models import Permission
# accounts/views.py
from .utils import assign_permissions  


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user and assign them roles and permissions
            user = serializer.save()
            assign_permissions(user)
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response({
            'error': 'Invalid data', 
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # This is still using session authentication
                return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'error': 'Invalid data', 
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Utility function to assign permissions based on role
def assign_permissions(user):
    permissions = []
    
    # Assigning permissions based on user role
    if user.role == 'Admin':
        permissions = Permission.objects.all()  # Admin gets all permissions
    elif user.role == 'Instructor':
        permissions = Permission.objects.filter(codename__in=['can_create_course', 'can_view_course'])
    elif user.role == 'Student':
        permissions = Permission.objects.filter(codename__in=['can_view_course', 'can_enroll_course'])

    # Assign permissions to the user
    user.user_permissions.set(permissions)
    user.save()
