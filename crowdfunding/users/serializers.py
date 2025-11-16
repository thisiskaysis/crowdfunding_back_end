from rest_framework import serializers
from .models import CustomUser, Child

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, read_only=True) #nested children

    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ('is_verified',)  # make is_verified read-only

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            date_of_birth=validated_data.get('date_of_birth'),
            profile_picture=validated_data.get('profile_picture'),
            password=validated_data['password']
        )
        return user