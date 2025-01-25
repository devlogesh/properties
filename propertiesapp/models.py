from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Userprofile(models.Model):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    user_type = models.CharField(max_length=255,null=True, choices=USER_TYPES, default='customer')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,db_column='user_id',null=True,blank=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50,unique=True,null=True,blank=True)
    mobile = models.CharField(max_length=15,unique=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    district = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    street = models.CharField(max_length=255,null=True,blank=True)
    pincode = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    address_line1 = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    verified = models.BooleanField(default=False)
    customer_number = models.CharField(max_length=255,null=True,blank=True)
    created_by_id = models.ForeignKey("Userprofile",on_delete=models.PROTECT,db_column='created_by_id',related_name='+',null=True,blank=True)
    updated_by_id = models.ForeignKey("Userprofile",on_delete=models.PROTECT,db_column='updated_by_id',related_name='+',null=True,blank=True)

    class Meta:
        db_table = 'userprofile'
        ordering = ['-id']

class AccessToken(models.Model):
    key = models.CharField(max_length=255)
    user_id = models.ForeignKey(User,on_delete=models.PROTECT,db_column='user_id')
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'accesstoken'
        ordering = ['-id']

class HouseProperty(models.Model):
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    reference_number = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=255)
    category = models.CharField(max_length=255,null=True,blank=True)
    house_type = models.CharField(max_length=255,null=True,blank=True)
    bathrooms = models.IntegerField(null=True,blank=True)
    facing = models.CharField(max_length=255,null=True,blank=True)
    parking = models.CharField(max_length=255,null=True,blank=True)
    area = models.BigIntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits = 19, decimal_places = 2, null=True,blank=True)
    negotiable = models.BooleanField(null=True,blank=True)
    furnishing = models.CharField(max_length=255,null=True,blank=True)
    total_floors  = models.IntegerField(null=True,blank=True)
    floor_number = models.IntegerField(null=True,blank=True)
    power_backup = models.BooleanField(null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    access_to_roads = models.CharField(max_length=255,null=True,blank=True)
    distance_from_road = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    utilities = models.CharField(max_length=255,null=True,blank=True)
    amenities = models.CharField(max_length=255,null=True,blank=True)
    encumbrance_certificate  = models.BooleanField(null=True,blank=True)#
    boundary = models.CharField(max_length=255,null=True,blank=True)
    water_resource = models.CharField(max_length=255,null=True,blank=True)
    zoning = models.CharField(max_length=255,null=True,blank=True)
    balcony = models.BooleanField(null=True,blank=True)
    property_age = models.CharField(max_length=255,null=True,blank=True)
    property_ownership = models.CharField(max_length=255,null=True,blank=True)
    approval_type = models.CharField(max_length=255,null=True,blank=True)
    nearby = models.CharField(max_length=255,null=True,blank=True)
    more_info = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255,null=True,blank=True)
    address_line1 = models.CharField(max_length=255,null=True,blank=True)
    street = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    district = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    pincode = models.CharField(max_length=255,null=True,blank=True)
    leading_image = models.CharField(max_length=255,null=True,blank=True)
    customer_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='customer_id',related_name='+',null=True,blank=True)
    created_by_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='created_by_id',related_name='+',null=True,blank=True)
    updated_by_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='updated_by_id',related_name='+',null=True,blank=True)
    property_type = models.CharField(max_length=255,default='residential')
    class Meta:
        db_table = 'house_property'
        ordering = ['-id']

class FarmLandProperty(models.Model):
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    reference_number = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=255)
    area = models.BigIntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits = 19, decimal_places = 2, null=True,blank=True)
    negotiable = models.BooleanField(null=True,blank=True)
    soil_type = models.CharField(max_length=255,null=True,blank=True)
    access_to_roads = models.CharField(max_length=255,null=True,blank=True)
    distance_from_road = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    water_resource = models.CharField(max_length=255,null=True,blank=True)
    irrigation_facilities = models.CharField(max_length=255,null=True,blank=True)
    electricity = models.BooleanField(null=True,blank=True)
    boundary = models.CharField(max_length=255,null=True,blank=True)
    encumbrance_certificate  = models.BooleanField(null=True,blank=True)
    property_ownership = models.CharField(max_length=255,null=True,blank=True)
    approval_type = models.CharField(max_length=255,null=True,blank=True)
    more_info = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    nearby = models.CharField(max_length=255,null=True,blank=True)
    zoning = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255,null=True,blank=True)
    address_line1 = models.CharField(max_length=255,null=True,blank=True)
    street = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    district = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    pincode = models.CharField(max_length=255,null=True,blank=True)
    leading_image = models.CharField(max_length=255,null=True,blank=True)
    customer_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='customer_id',related_name='+',null=True,blank=True)
    created_by_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='created_by_id',related_name='+',null=True,blank=True)
    updated_by_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='updated_by_id',related_name='+',null=True,blank=True)
    property_type = models.CharField(max_length=255,default='farmland')

    class Meta:
        db_table = 'farmland_property'
        ordering = ['-id']

class PlotProperty(models.Model):
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    reference_number = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=255)
    plot_number = models.IntegerField(null=True,blank=True)
    facing = models.CharField(max_length=255,null=True,blank=True)
    price = models.DecimalField(max_digits = 19, decimal_places = 2, null=True,blank=True)
    north_south_length = models.DecimalField(max_digits = 19, decimal_places = 2, null=True,blank=True)
    east_west_length = models.DecimalField(max_digits = 19, decimal_places = 2, null=True,blank=True)
    area = models.BigIntegerField(null=True,blank=True)
    negotiable = models.BooleanField(null=True,blank=True)
    access_to_roads = models.CharField(max_length=255,null=True,blank=True)
    distance_from_road = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    utilities = models.CharField(max_length=255,null=True,blank=True)
    amenities = models.CharField(max_length=255,null=True,blank=True)
    encumbrance_certificate  = models.BooleanField(null=True,blank=True)
    boundary = models.CharField(max_length=255,null=True,blank=True)
    water_resource = models.CharField(max_length=255,null=True,blank=True)
    property_ownership = models.CharField(max_length=255,null=True,blank=True)
    approval_type = models.CharField(max_length=255,null=True,blank=True)
    more_info = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    nearby = models.CharField(max_length=255,null=True,blank=True)
    zoning = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255,null=True,blank=True)
    address_line1 = models.CharField(max_length=255,null=True,blank=True)
    street = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    district = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    pincode = models.CharField(max_length=255,null=True,blank=True)
    leading_image = models.CharField(max_length=255,null=True,blank=True)
    customer_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='customer_id',related_name='+',null=True,blank=True)
    created_by_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='created_by_id',related_name='+',null=True,blank=True)
    updated_by_id = models.ForeignKey(Userprofile,on_delete=models.PROTECT,db_column='updated_by_id',related_name='+',null=True,blank=True)
    property_type = models.CharField(max_length=255,default='plot')
    class Meta:
        db_table = 'plot_property'
        ordering = ['-id']


class PropertyMedia(models.Model):
    
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    house_property_id = models.ForeignKey(HouseProperty, on_delete=models.CASCADE,db_column='house_property_id',null=True,blank=True)
    farmland_property_id = models.ForeignKey(FarmLandProperty, on_delete=models.CASCADE,db_column='farmland_property_id',null=True,blank=True)
    plot_property_id = models.ForeignKey(PlotProperty, on_delete=models.CASCADE,db_column='plot_property_id',null=True,blank=True)
    media_url = models.CharField(max_length=255)
    is_image = models.BooleanField(default=False)
    is_video = models.BooleanField(default=False)
    is_document = models.BooleanField(default=False)

    class Meta:
        db_table = 'property_media'
        ordering = ['-id']

