from datetime import datetime
from .models import *
import random

def reference_number():
    reference_num = 'PROP'+str(datetime.now().date()).replace('-','')+str(random.randint(10000,99999))
    prop = Property.objects.filter(reference_number=reference_num)
    if len(prop) == 0:
        return reference_num
    else:
        return reference_number()

def propertyParser(request):
    data = request.data
    reference_number_ = reference_number()
    parser_data = {
        'reference_number':data['reference_number'] if data.get('reference_number') else reference_number_,
        'transaction_type':data['transaction_type'] if data.get('transaction_type') else None,
        'facing':data['facing']['value'] if data.get('facing') else None,
        'area':data['area'] if data.get('area') else 0,
        'price':data['price'] if data.get('price') else 0.00,
        'negotiable':data['negotiable'] if data.get('negotiable') else False,
        'location':data['location'] if data.get('location') else None,
        'access_to_roads':data['access_to_roads']['value'] if data.get('access_to_roads') else None,
        'distance_from_road':data['distance_from_road'] if data.get('distance_from_road') else None,
        'utilities':",".join(data['utilities']) if data.get('utilities') else None,
        'amenities':",".join(data['amenities']) if data.get('amenities') else None,
        'encumbrance_certificate':data['encumbrance_certificate'] if data.get('encumbrance_certificate') else False,
        'boundary':data['boundary'] if data.get('boundary') else None,
        'water_resource':",".join(data['water_resource']) if data.get('water_resource') else None,
        'zoning':data['zoning'] if data.get('transaction_type') else None,
        'property_ownership':data['property_ownership']['value'] if data.get('property_ownership') else None,
        'approval_type':data['approval_type']['value'] if data.get('approval_type') else None,
        'nearby':data['nearby'] if data.get('nearby') else None,
        'more_info':data['more_info'] if data.get('more_info') else None,
        'status':data['status']['value'] if data.get('status') else None,
        'address_line1':data['address']['address_line1'] if data.get('address') else None,
        'street':data['address']['street'] if data.get('address') else None,
        'city':data['address']['city'] if data.get('address') else None,
        'district':data['address']['district'] if data.get('address') else None,
        'state':data['address']['state'] if data.get('address') else None,
        'country':data['address']['country'] if data.get('address') else None,
        'pincode':data['address']['pincode'] if data.get('address') else None,
        'category':data['category']['value'] if data.get('category') else None,
        'house_type':data['house_type']['value'] if data.get('house_type') else None,
        'bathrooms':data['bathrooms'] if data.get('bathrooms') else 0,
        'parking':",".join(data['parking']) if data.get('parking') else None,
        'furnishing':data['furnishing'] if data.get('furnishing') else None,
        'total_floors':data['total_floors'] if data.get('total_floors') else 0,
        'floor_number':data['floor_number'] if data.get('floor_number') else None,
        'power_backup':data['power_backup'] if data.get('power_backup') else False,
        'balcony':data['balcony'] if data.get('balcony') else False,
        'property_age':data['property_age'] if data.get('property_age') else None,
        'plot_number':data['plot_number'] if data.get('plot_number') else 0,
        'north_south_length':data['north_south_length'] if data.get('north_south_length') else 0.00,
        'east_west_length':data['east_west_length'] if data.get('east_west_length') else 0.00,
        'soil_type':data['soil_type']['value'] if data.get('soil_type') else None,
        'irrigation_facilities':",".join(data['irrigation_facilities']) if data.get('irrigation_facilities') else None,
        'electricity':data['electricity'] if data.get('electricity') else False

    }
    return parser_data