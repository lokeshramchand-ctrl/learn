from rest_framework import serializers
from accounts.models import User 


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField() 
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # Create and return a new user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            
        )
        return user
