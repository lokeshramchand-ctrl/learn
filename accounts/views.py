from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import  LoginSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        # Validate the serializer
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            # Authenticate the user
            user_obj = authenticate(username=username, password=password)

            if user_obj:
                token, _= Token.objects.get_or_create(user=user_obj)
                print(token)
                # You can add a token generation mechanism here, e.g., JWT
                return Response({"status": True, "data": {'token': str(token)}})
            else:
                return Response({"status": False, "message": "Invalid credentials"}, status=400)
        else:
            return Response({"status": False, "message": "Invalid input", "errors": serializer.errors}, status=400)

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        # Validate the serializer
        if serializer.is_valid():
            user = serializer.save()  # Save the new user
            token, _ = Token.objects.get_or_create(user=user)  # Generate token
            return Response({"status": True, "data": {"username": user.username, "token": str(token)}})
        else:
            return Response({"status": False, "message": "Invalid input", "errors": serializer.errors}, status=400)

"""
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
"""