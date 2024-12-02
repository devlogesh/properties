from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('user_list/',ListUserProfile.as_view(),name='user_list'),
    path('user_create/',CreateUserProfile.as_view(),name='user_create'),
    path('user_get/<int:pk>/',GetUpdateUserProfile.as_view(),name='user_get_update'),
    path('property_list/',ListProperty.as_view(),name='property_list'),
    path('property_create/',CreateProperty.as_view(),name='property_create'),
    path('property_get/<int:pk>/',GetUpdateProperty.as_view(),name='property_get_update')
]

urlpatterns = format_suffix_patterns(urlpatterns)