
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

from django.utils.decorators import method_decorator
from properties.decorator import bearer_token_required
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token







class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
        


class ListUserProfile(generics.ListAPIView):
    queryset = Userprofile.objects.filter(active=True)
    serializer_class = UserProfileSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super(ListUserProfile, self).get_queryset()
        user_type = self.request.query_params.get('user_type')
        mobile_number = self.request.query_params.get('mobile_number')
        customer_number = self.request.query_params.get('customer_number')
        username = self.request.query_params.get('customer_name')
        if user_type:
            if user_type=='customer':
                return queryset.filter(user_type='customer')
            else:
                return queryset.exclude(user_type='customer')
        if mobile_number:
            return queryset.filter(mobile__icontains=mobile_number)
        if customer_number:
            return queryset.filter(customer_number__icontains=customer_number)
        if username:
            return queryset.filter(username__icontains=customer_number)
        
        return queryset

class CreateUserProfile(APIView):
    def post(self,request):
        val = user_params(request)
        user_data = {'username' : val['mobile'],'email' : val['email'],'password' : val['password']}
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
        
# @method_decorator(csrf_exempt, name='dispatch')
class UserLoginAPIView(APIView):

    def post(self,request,**kwargs):
        user_params = request.data
        username = user_params.get('username')
        password = user_params.get('password')

        if username and password:
            user = authenticate(username=user_params['username'],password=user_params['password'])
            if user:
                login(request,user)
                profile = Userprofile.objects.get(user_id=user.id)

                token_id = Token.objects.filter(user_id = user.id)
                if len(token_id)>0:
                    token_id.delete()
                token,create = Token.objects.get_or_create(user=user)
                token_obj = AccessToken.objects.create(user_id=user,key=token.key)
                return Response({'user_id':user.id,'token':token.key}, status=status.HTTP_200_OK)
            else:
                errors = {'message':'Invalid Credentials..'}
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            errors = {'message':'Username and Password should not be empty..'}
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
                 
class GetUpdateUserProfile(APIView):
    def get_object(self,pk):
        return Userprofile.objects.get(pk=pk)

    @method_decorator(bearer_token_required)
    def get(self,request,pk,format=None):
        try:
            userprofile = self.get_object(pk)
            serializer = UserProfileSerializer(userprofile)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        
    @method_decorator(bearer_token_required)
    def put(self,request,pk,format=None):
        try:
            userprofile = self.get_object(pk)
            print(request.data)
            val = user_params(request)
            serializer = UserProfileSerializer(userprofile,data=val)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        
# @method_decorator(bearer_token_required,name='dispatch') 
class ListHouseProperty(generics.ListAPIView):
    
    queryset = HouseProperty.objects.filter(active=True)
    serializer_class = HousePropertyListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        reference_number = self.request.query_params.get('reference_number')
        if reference_number:
            return queryset.filter(reference_number=reference_number)
        return queryset
    
class CreateHouseProperty(APIView):
    @method_decorator(bearer_token_required)
    def post(self,request):
        val = house_propertyParser(request)
        
        print(val)
        # file = request.FILES['image']
        serializer = HousePropertyCreateSerializer(data=val)
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
        
class GetUpdateHouseProperty(APIView):
    def get_object(self,pk):
        return HouseProperty.objects.get(pk=pk)
    
    @method_decorator(bearer_token_required)
    def get(self,request,pk,format=None):
        print(request.user)
        try:
            property = self.get_object(pk)
            serializer = HousePropertyListSerializer(property)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(bearer_token_required)
    def put(self,request,pk,format=None):
        try:
            property = self.get_object(pk)
            print(request.data)
            data = house_propertyParser(request)
            if 'reference_number' not in  data:
                content = {'message': 'Reference Number Required'}
                return Response(content,status=status.HTTP_400_BAD_REQUEST)
            serializer =HousePropertyCreateSerializer(property,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        
# @method_decorator(bearer_token_required,name='dispatch') 
class ListFarmLandProperty(generics.ListAPIView):
    
    queryset = FarmLandProperty.objects.filter(active=True)
    serializer_class = FarmLandPropertyListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        reference_number = self.request.query_params.get('reference_number')
        if reference_number:
            return queryset.filter(reference_number=reference_number)
        return queryset
    
class CreateFarmLandProperty(APIView):
    @method_decorator(bearer_token_required)
    def post(self,request):
        val = farmland_propertyParser(request)
        
        print(val)
        # file = request.FILES['image']
        serializer = FarmLandPropertyCreateSerializer(data=val)
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
        
class GetUpdateFarmLandProperty(APIView):
    def get_object(self,pk):
        return FarmLandProperty.objects.get(pk=pk)
    
    @method_decorator(bearer_token_required)
    def get(self,request,pk,format=None):
        print(request.user)
        try:
            property = self.get_object(pk)
            serializer = FarmLandPropertyListSerializer(property)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(bearer_token_required)
    def put(self,request,pk,format=None):
        try:
            property = self.get_object(pk)
            print(request.data)
            data = farmland_propertyParser(request)
            if 'reference_number' not in  data:
                content = {'message': 'Reference Number Required'}
                return Response(content,status=status.HTTP_400_BAD_REQUEST)
            serializer =FarmLandPropertyCreateSerializer(property,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        
# @method_decorator(bearer_token_required,name='dispatch') 
class ListPlotProperty(generics.ListAPIView):
    
    queryset = PlotProperty.objects.filter(active=True)
    serializer_class = PlotPropertyListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        reference_number = self.request.query_params.get('reference_number')
        if reference_number:
            return queryset.filter(reference_number=reference_number)
        return queryset
    
class CreatePlotProperty(APIView):
    @method_decorator(bearer_token_required)
    def post(self,request):
        val = plot_propertyParser(request)
        
        print(val)
        # file = request.FILES['image']
        serializer = PlotPropertyCreateSerializer(data=val)
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
        
class GetUpdatePlotProperty(APIView):
    def get_object(self,pk):
        return PlotProperty.objects.get(pk=pk)
    
    @method_decorator(bearer_token_required)
    def get(self,request,pk,format=None):
        print(request.user)
        try:
            property = self.get_object(pk)
            serializer = PlotPropertyListSerializer(property)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(bearer_token_required)
    def put(self,request,pk,format=None):
        try:
            property = self.get_object(pk)
            print(request.data)
            data = plot_propertyParser(request)
            if 'reference_number' not in  data:
                content = {'message': 'Reference Number Required'}
                return Response(content,status=status.HTTP_400_BAD_REQUEST)
            serializer =PlotPropertyCreateSerializer(property,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except:
            content = {'message': 'No Record Found'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        

class GetPropertyByRef(APIView):
    def post(self,request):
        reference_number = request.data.get('reference_number')
        if reference_number:
            house_list = HouseProperty.objects.filter(reference_number=reference_number)
            if len(house_list) > 0:
                serializer = HousePropertyListSerializer(house_list[0])
                return Response(serializer.data,status=status.HTTP_200_OK)
            farmland_list = FarmLandProperty.objects.filter(reference_number=reference_number)
            if len(farmland_list) > 0:
                serializer = FarmLandPropertyListSerializer(farmland_list[0])
                return Response(serializer.data,status=status.HTTP_200_OK)
            plot_list = PlotProperty.objects.filter(reference_number=reference_number)
            if len(plot_list) > 0:
                serializer = PlotPropertyListSerializer(plot_list[0])
                return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            content = {'message': 'Please Enter Property Number'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        