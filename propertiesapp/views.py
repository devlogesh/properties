import random
from .models import *
from .serializers import *
from .functions import *
import os
from django.conf import settings
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, generics,filters,authentication, permissions


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
        


class ListUserProfile(generics.ListAPIView):
    queryset = Userprofile.objects.filter(active=True)
    serializer_class = UserProfileSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super(ListUserProfile, self).get_queryset()
        state = self.request.query_params.get('state')
        if state:
            return queryset.filter(state__icontains=state)
        return queryset

class CreateUserProfile(APIView):
    def post(self,request):
        val = request.data
        user_data = {'username' : val.get('mobile'),'email' : val.get('email'),'password' : val.get('password')}
        user_serializer = UserCreateSerializer(data=user_data)
        if user_serializer.is_valid():            
            serializer = UserProfileSerializer(data=val)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.create(**user_serializer.validated_data)
                user.set_password(user_data['password'])
                user.save()
                user_profile = Userprofile.objects.get(id=serializer.data['id'])
                user_profile.user_id = user
                user_profile.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user_serializer.errors,status.HTTP_400_BAD_REQUEST)

class GetUpdateUserProfile(APIView):
    def get_object(self,pk):
        return Userprofile.objects.get(pk=pk)

    def get(self,request,pk,format=None):
        try:
            userprofile = self.get_object(pk)
            serializer = UserProfileSerializer(userprofile)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        try:
            userprofile = self.get_object(pk)
            print(request.data)

            serializer = UserProfileSerializer(userprofile,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        


class ListProperty(generics.ListAPIView):
    queryset = Property.objects.filter(active=True)
    serializer_class = PropertyListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super(ListProperty, self).get_queryset()
        reference_number = self.request.query_params.get('reference_number')
        if reference_number:
            return queryset.filter(reference_number=reference_number)
        return queryset
    
class CreateProperty(APIView):
    def post(self,request):
        val = propertyParser(request)
        
        print(val)
        # file = request.FILES['image']
        serializer = PropertyCreateSerializer(data=val)
        if serializer.is_valid():
            serializer.save()
            # if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'images')):
            #     os.makedirs(os.path.join(settings.MEDIA_ROOT, 'images'))
            # file_path = os.path.join(settings.MEDIA_ROOT, 'images', file.name)
            # with open(file_path, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            # property.leading_image = file_path
            serializer_dict = serializer.data
            return Response(serializer_dict,status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        
class GetUpdateProperty(APIView):
    def get_object(self,pk):
        return Property.objects.get(pk=pk)

    def get(self,request,pk,format=None):
        try:
            property = self.get_object(pk)
            serializer = PropertyListSerializer(property)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        try:
            property = self.get_object(pk)
            print(request.data)
            data = propertyParser(request)
            serializer = PropertyCreateSerializer(property,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)