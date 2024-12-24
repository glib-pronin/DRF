from rest_framework import serializers
from .models import Trainer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.contrib.auth.models import User 


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields ="__all__"

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields =["username", "email", "password", "confirm_password"]

    def validate(self, data):
        if data['password']!=data['confirm_password']:
            raise serializers.ValidationError("Паролі не збігаються")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password= validated_data['password']
        )
        return user

# def encode():
#     model = TrainerModel('Alex', 'Strong man')
#     model_sr= TrainerSerializer(model)
#     print(model_sr.data)
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"name":"Serge","content":"Inteligent man"}')
#     data = JSONParser().parse(stream)
#     serializer = TrainerSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)