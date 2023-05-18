from django.contrib.auth.models import User, BaseUserManager

from django.conf import settings

from rest_framework import serializers

from .models import User
from .models import Proprietaire
from .models import Etudiant
from rest_framework import serializers
from django.contrib.auth import get_user_model

 

""""

from .models import Offre

 

class OfferSerializer(serializers.ModelSerializer):

    class Meta:

        model = Offre

        fields = ('__all__')

"""
"""class SignupSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=30)

    email = serializers.CharField(max_length=30)

    password  = serializers.CharField(max_length=128, write_only=True)

 

    class Meta:

        model = User

        fields = ['username', 'email', 'password']

 

    def create(self, validated_data):

        user = User.objects.create_user(

            username=validated_data['username'],

            email=validated_data['email'],

            password=validated_data['password'],

        )

        return user
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Proprietaire, Etudiant

#User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type']

class ProprietaireSignupSerializer(SignupSerializer):
    # Ajoutez des champs spécifiques aux propriétaires si nécessaire
    class Meta(SignupSerializer.Meta):
        model = Proprietaire

class EtudiantSignupSerializer(SignupSerializer):
    # Ajoutez des champs spécifiques aux étudiants si nécessaire
    class Meta(SignupSerializer.Meta):
        model = Etudiant



