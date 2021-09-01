from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


UserModel=get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        return user
    
    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( 'username', 'password', 'email', 'first_name', 'last_name')