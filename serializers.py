
from rest_framework import serializers
from models import *

from django.contrib.auth.models import User

class instanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instance
        fields=("instanceID","game")

class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("pk","name","instance","score")


