from rest_framework import serializers

from django.contrib.auth import get_user_model, password_validation, hashers
User = get_user_model()

# Serializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        # Remove plain text password and password_confirmation from the dictionary of fields (data)
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        # Check plain text password against the password_confirmation, raise error if dont match
        if password != password_confirmation:
            raise serializers.ValidationError({ 'password_confirmation': 'Passwords do not match.' })

        # If passwords match, run validators against the password
        password_validation.validate_password(password)

        # Hash the plain text password and add it back to the data dictionary
        data['password'] = hashers.make_password(password)

        # Return the data
        return data

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password_confirmation', 'first_name', 'last_name')