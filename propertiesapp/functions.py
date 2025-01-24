from datetime import datetime
from .models import *
import random

def reference_number(model):
    
    if model == 'house':
        reference_num = 'HOUS'+str(datetime.now().date()).replace('-','')+str(random.randint(10000,99999))
        prop = HouseProperty.objects.filter(reference_number=reference_num)
    if model == 'farmland':
        reference_num = 'FARM'+str(datetime.now().date()).replace('-','')+str(random.randint(10000,99999))
        prop = FarmLandProperty.objects.filter(reference_number=reference_num)
    if model == 'plot':
        reference_num = 'PLOT'+str(datetime.now().date()).replace('-','')+str(random.randint(10000,99999))
        prop = PlotProperty.objects.filter(reference_number=reference_num)
    if len(prop) == 0:
        return reference_num
    else:
        return reference_number(model)
    
def random_customer_number():
    random_number = ''.join(random.choices('0123456789', k=8))
    user = Userprofile.objects.filter(customer_number=random_number)
    if len(user) == 0:
        return random_number
    else:
        return random_customer_number()
    
def user_params(request):
    val = request.data
    address = val.get('address')
    customer_number = random_customer_number()
    parser_data = {
        'mobile':val.get('mobile_number'),
        'email':val.get('e_mail'),
        'password':val.get('password','Admin@123'),
        'username':val.get('username') if 'username' in val else val.get('customer_name'),
        "user_type":val.get('user_type','customer'),
        'location':val.get('location'),
        # address
        'state':address.get('state'),
        'district':address.get('district'),
        'city':address.get('city'),
        'street':address.get('street'),
        'pincode':address.get('pincode'),
        'address_line1':address.get('address_line1'),
        'country':address.get('country'),
        'customer_number':val['customer_number'] if val.get('customer_number') else str(customer_number),
        'created_by_id':val.get('created_by_id',None),
        'updated_by_id':val.get('updated_by_id',None),
        
    }

    return parser_data


def house_propertyParser(request):
    data = request.data
    reference_number_ = reference_number('house')
    address = data.get('address')
    parser_data = {
        'reference_number':data['reference_number'] if data.get('reference_number') else reference_number_,
        'transaction_type':data.get('transaction_type',None),
        'category':data.get('category',None),
        'house_type':data.get('house_type',None),
        'bathrooms':data.get('bathrooms',0),
        'facing':data.get('facing',None),
        'parking':",".join(data['parking']) if data.get('parking') and len(data.get('parking')) > 0 else None,
        'area':data.get('area',0),
        'price':data.get('price',0.00),
        'negotiable':data.get('negotiable',False),
        'furnishing':data.get('furnishing',None),
        'total_floors':data.get('total_floors',0),
        'floor_number':data.get('floor_number',0),
        'power_backup':data.get('power_backup',False),
        'location':data.get('location',None),
        'access_to_roads':data.get('access_to_roads',None),
        'distance_from_road':data.get('distance_from_road',0.00),
        'utilities':",".join(data['utilities']) if data.get('utilities') and len(data.get('utilities')) > 0 else None,
        'amenities':",".join(data['amenities']) if data.get('amenities') and len(data.get('amenities')) > 0 else None,
        'encumbrance_certificate':data.get('encumbrance_certificate',False),
        'boundary':data.get('boundary',False),
        'water_resource':",".join(data['water_resource']) if data.get('water_resource') and len(data.get('water_resource')) > 0 else None,
        'zoning':data.get('zoning',None),
        'balcony':data.get('balcony',False),
        'property_age':data.get('property_age',None),
        'property_ownership':data.get('property_ownership',None),
        'approval_type':data.get('approval_type',None),
        'nearby':data.get('nearby',None),
        'more_info':data.get('more_info',None),
        'status':data.get('status',None),
        'address_line1':address.get('address_line1',None),
        'street':address.get('street',None),
        'city':address.get('city',None),
        'district':address.get('district',None),
        'state':address.get('state',None),
        'country':address.get('country',None),
        'pincode':address.get('pincode',None),
        'customer_id':data.get('customer_id',None),
        'created_by_id':data.get('created_by_id',None),
        'updated_by_id':data.get('updated_by_id',None), 

    }
    return parser_data

def farmland_propertyParser(request):
    data = request.data
    reference_number_ = reference_number('farmland')
    address = data.get('address')
    parser_data = {
        'reference_number':data['reference_number'] if data.get('reference_number') else reference_number_,
        'transaction_type':data.get('transaction_type',None),
        'area':data.get('area',0),
        'price':data.get('price',0.00),
        'negotiable':data.get('negotiable',False),
        'soil_type':data.get('soil_type',None),
        'access_to_roads':data.get('access_to_roads',None),
        'distance_from_road':data.get('distance_from_road',0.00),
        'water_resource':",".join(data['water_resource']) if data.get('water_resource') and len(data.get('water_resource')) else None,
        'irrigation_facilities':",".join(data['irrigation_facilities']) if data.get('irrigation_facilities') and len(data.get('irrigation_facilities')) > 0 else None,
        'electricity':data.get('electricity',False),
        'boundary':data.get('boundary',None),
        'encumbrance_certificate':data.get('encumbrance_certificate',False),
        'property_ownership':data.get('property_ownership',None),
        'approval_type':data.get('approval_type',None),
        'more_info':data.get('more_info',None),
        'location':data.get('location',None),
        'nearby':data.get('nearby',None),
        'zoning':data.get('zoning',None),
        'status':data.get('status',None),
        'address_line1':address.get('address_line1',None),
        'street':address.get('street',None),
        'city':address.get('city',None),
        'district':address.get('district',None),
        'state':address.get('state',None),
        'country':address.get('country',None),
        'pincode':address.get('pincode',None),
        'customer_id':data.get('customer_id',None),
        'created_by_id':data.get('created_by_id',None),
        'updated_by_id':data.get('updated_by_id',None),
    }

    return parser_data

def plot_propertyParser(request):
    data = request.data
    reference_number_ = reference_number('plot')
    address = data.get('address')
    parser_data = {
        'reference_number':data['reference_number'] if data.get('reference_number') else reference_number_,
        'transaction_type':data.get('transaction_type',None),
        'plot_number':data.get('plot_number',0),
        'facing':data.get('facing',None),
        'price':data.get('price',0.00),
        'north_south_length':data.get('north_south_length',0.00),
        'east_west_length':data.get('east_west_length',0.00),
        'area':data.get('area',0),
        'negotiable':data.get('negotiable',False),
        'access_to_roads':data.get('access_to_roads',None),
        'distance_from_road':data.get('distance_from_road',0.00),
        'utilities':",".join(data['utilities']) if data.get('utilities') and len(data.get('utilities')) > 0 else None,
        'amenities':",".join(data['amenities']) if data.get('amenities') and len(data.get('amenities')) > 0 else None,
        'encumbrance_certificate':data.get('encumbrance_certificate',False),
        'boundary':data.get('boundary',None),
        'water_resource':",".join(data['water_resource']) if data.get('water_resource') and len(data.get('water_resource')) > 0 else None,
        'property_ownership':data.get('property_ownership',None),
        'approval_type':data.get('approval_type',None),
        'more_info':data.get('more_info',None),
        'location':data.get('location',None),
        'nearby':data.get('nearby',None),
        'zoning':data.get('zoning',None),
        'status':data.get('status',None),
        'address_line1':address.get('address_line1',None),
        'street':address.get('street',None),
        'city':address.get('city',None),
        'district':address.get('district',None),
        'state':address.get('state',None),
        'country':address.get('country',None),
        'pincode':address.get('pincode',None),
        'customer_id':data.get('customer_id',None),
        'created_by_id':data.get('created_by_id',None),
        'updated_by_id':data.get('updated_by_id',None),
    }

    return parser_data