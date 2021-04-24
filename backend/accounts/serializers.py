from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation, authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('user_name', 'email', 'first_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            user_name=validated_data['user_name'],
            first_name=validated_data['first_name'],
            password=validated_data['password'],
        )
        user.save()
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)
        
    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credentials are not valid')
     
        self.context['user'] = user
        return data
    

class PasswordChangeSerializer(serializers.Serializer):
    model = get_user_model()
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
class PasswordSendSerializer(serializers.Serializer):
    email = serializers.EmailField()