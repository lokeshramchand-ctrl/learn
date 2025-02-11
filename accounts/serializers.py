from rest_framework import serializers
from accounts.models import User  # Import your custom User model
from django.contrib.auth.models import Permission

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'required': True},
        }

    def create(self, validated_data):
        role = validated_data.get('role', 'Student')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role,
        )

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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


