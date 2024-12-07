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


    class Meta:
        db_table = 'userprofile'
        ordering = ['-id']

class Property(models.Model):
    # common
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    reference_number = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=255)
    facing = models.CharField(max_length=255,null=True,blank=True)
    area = models.BigIntegerField(default=0)
    price = models.DecimalField(max_digits = 19, decimal_places = 2, default=0.00)
    negotiable = models.BooleanField(default=False)#
    location = models.CharField(max_length=255,null=True,blank=True)
    access_to_roads = models.CharField(max_length=255,null=True,blank=True)
    distance_from_road = models.DecimalField(max_digits = 5, decimal_places = 2, default=0.00)
    utilities = models.CharField(max_length=255,null=True,blank=True)
    amenities = models.CharField(max_length=255,null=True,blank=True)
    encumbrance_certificate  = models.BooleanField(default=False)#
    boundary = models.CharField(max_length=255,null=True,blank=True)
    water_resource = models.CharField(max_length=255,null=True,blank=True)
    zoning = models.CharField(max_length=255,null=True,blank=True)
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

    # home
    category = models.CharField(max_length=255,null=True,blank=True)
    house_type = models.CharField(max_length=255,null=True,blank=True)
    bathrooms = models.IntegerField(default=0)#
    parking = models.CharField(max_length=255,null=True,blank=True)
    furnishing = models.CharField(max_length=255,null=True,blank=True)
    total_floors  = models.IntegerField(default=0)
    floor_number = models.IntegerField(null=True,blank=True)
    power_backup = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    property_age = models.CharField(max_length=255,null=True,blank=True)

    # plot
    plot_number = models.IntegerField(default=0)#
    north_south_length = models.DecimalField(max_digits = 19, decimal_places = 2, default=0.00)
    east_west_length = models.DecimalField(max_digits = 19, decimal_places = 2, default=0.00)

    # formland
    soil_type = models.CharField(max_length=255,null=True,blank=True)
    irrigation_facilities = models.CharField(max_length=255,null=True,blank=True)
    electricity = models.BooleanField(default=False)

    class Meta:
        db_table = 'property'
        ordering = ['-id']

class PropertyMedia(models.Model):
    
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE,db_column='property_id')
    media_url = models.CharField(max_length=255)
    is_image = models.BooleanField(default=False)
    is_video = models.BooleanField(default=False)
    is_document = models.BooleanField(default=False)

    class Meta:
        db_table = 'property_media'
        ordering = ['-id']

