from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    #Customize the serializer class for get email and user_id (jwt-create)

    def validate(self, attrs):
        valifated_data =  super().validate(attrs)
        valifated_data['email'] = self.user.email
        valifated_data['user_id'] = self.user.id
        return valifated_data

class ChangePasswordSerializer(serializers.Serializer):
    #customize serializer class for change password

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password1'):
            raise serializers.ValidationError(
                {'detail':'password dosent match'})
        try:
            validate_password(attrs.get('new_password'))
        except exceptions.ValidationError as e :
            raise serializers.ValidationError(
                {'new_password': list(e.messages)})
        return super().validate(attrs)

