from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    #Customize the serializer class for get email and user_id (jwt-create)

    def validate(self, attrs):
        valifated_data =  super().validate(attrs)
        valifated_data['email'] = self.user.email
        valifated_data['user_id'] = self.user.id
        return valifated_data