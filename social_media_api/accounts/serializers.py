from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create user with the provided data
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        # Create and return a token for the new user
        Token.objects.create(user=user)
        return user

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('Invalid Credentials')
        attrs['user'] = user
        return attrs
