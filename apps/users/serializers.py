from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'last_login', 'username',
                  'first_name', 'last_name', 'email',
                  'date_joined', 'profile_image', 'phone_number',
                  'verify')