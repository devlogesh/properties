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

class UserProfileLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['id','username','mobile','customer_number']

class HousePropertyListSerializer(serializers.ModelSerializer):
    customer_id = UserProfileLookupSerializer()
    created_by_id = UserProfileLookupSerializer()
    updated_by_id = UserProfileLookupSerializer()
    class Meta:
        model = HouseProperty
        fields = '__all__'

class HousePropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseProperty
        fields = '__all__'

class FarmLandPropertyListSerializer(serializers.ModelSerializer):
    customer_id = UserProfileLookupSerializer()
    created_by_id = UserProfileLookupSerializer()
    updated_by_id = UserProfileLookupSerializer()
    class Meta:
        model = FarmLandProperty
        fields = '__all__'

class FarmLandPropertyCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FarmLandProperty
        fields = '__all__'


class PlotPropertyListSerializer(serializers.ModelSerializer):
    customer_id = UserProfileLookupSerializer()
    created_by_id = UserProfileLookupSerializer()
    updated_by_id = UserProfileLookupSerializer()
    class Meta:
        model = PlotProperty
        fields = '__all__'

class PlotPropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotProperty
        fields = '__all__'