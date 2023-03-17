from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # Levanta el serializer apuntando a nuestro modelo
    class Meta:
        model = models.UserProfile
        # Definimos los campos que haremos accesibles en el modelo
        fields = ("id", "email", "name", "password")
        """
        Declaramos argumentos extra para que la pass
        no sea de tipo lectura de manera que no sea devuelta en algun metodo retrieve,
        luego seteamos el estilo a password para que
        se muestre como puntitos en el navegador
        """
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ("id", "user_profile", "status_text", "created_on")
        extra_kwargs = {"user_profile": {"read_only": True}}
