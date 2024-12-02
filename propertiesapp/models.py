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
    username = models.CharField(max_length=100,unique=True)
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
    
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    reference_number = models.CharField(max_length=255)
    property_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    owner_phone_number = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255,null=True,blank=True)
    detailed_description = models.TextField(null=True)
    min_price = models.DecimalField(max_digits = 19, decimal_places = 2, default=0.00)
    max_price = models.DecimalField(max_digits = 19, decimal_places = 2, default=0.00)
    location = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    district = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    street = models.CharField(max_length=255,null=True,blank=True)
    pincode = models.CharField(max_length=255,null=True,blank=True)
    property_type = models.CharField(max_length=255,null=True,blank=True)
    number_of_enquires = models.IntegerField(default=0)
    negotiation_percentage = models.DecimalField(max_digits = 5, decimal_places = 2, default=0.00)
    status = models.CharField(max_length=255,null=True,blank=True)
    leading_image = models.CharField(max_length=255,null=True,blank=True)
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

