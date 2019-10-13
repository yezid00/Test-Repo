
from rest_framework import serializers
from project.accounts.models import User
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
        ]

    def validate_password1(self, password1):
        validate_password(password1)
        return password1

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def save(self, request):
        password1 = self.validated_data.pop('password1')
        self.validated_data.pop('password2')

        return User.objects.create_user(
            email=self.validated_data.get('email'),
            password=password1
        )

