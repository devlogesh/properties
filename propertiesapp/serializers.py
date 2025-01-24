from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        exclude = ['user_id']

class HousePropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseProperty
        fields = '__all__'

class HousePropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseProperty
        fields = '__all__'

class FarmLandPropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmLandProperty
        fields = '__all__'

class FarmLandPropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmLandProperty
        fields = '__all__'


class PlotPropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotProperty
        fields = '__all__'

class PlotPropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotProperty
        fields = '__all__'