from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('user_list/',ListUserProfile.as_view(),name='user_list'),
    path('user_create/',CreateUserProfile.as_view(),name='user_create'),
    path('user_get/<int:pk>/',GetUpdateUserProfile.as_view(),name='user_get_update'),
    path('login/',UserLoginAPIView.as_view(),name="login"),#Login
    # house
    path('house_property_list/',ListHouseProperty.as_view(),name='house_property_list'),
    path('house_property_create/',CreateHouseProperty.as_view(),name='house_property_create'),
    path('house_property_get/<int:pk>/',GetUpdateHouseProperty.as_view(),name='house_property_get'),
    # farmland
    path('farmland_property_list/',ListFarmLandProperty.as_view(),name='farmland_property_list'),
    path('farmland_property_create/',CreateFarmLandProperty.as_view(),name='farmland_property_create'),
    path('farmland_property_get/<int:pk>/',GetUpdateFarmLandProperty.as_view(),name='farmland_property_get'),
    # plot
    path('plot_property_list/',ListPlotProperty.as_view(),name='plot_property_list'),
    path('plot_property_create/',CreatePlotProperty.as_view(),name='plot_property_create'),
    path('plot_property_get/<int:pk>/',GetUpdatePlotProperty.as_view(),name='plot_property_get'),
]

urlpatterns = format_suffix_patterns(urlpatterns)