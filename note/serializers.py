from .models import Note , Customer
from rest_framework import serializers
from django.contrib.auth.models import User 

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Note 
        fields="__all__"

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def create(self, validated_data):
            user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'] )

            Customer.objects.create(
                user=user,
                name=user.username,
                email=user.email )
            return user
        
            