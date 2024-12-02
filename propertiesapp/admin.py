from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

@admin.register(Userprofile)
class UserprofileAdmin(ImportExportModelAdmin):
    pass

@admin.register(Property)
class PropertyAdmin(ImportExportModelAdmin):
    pass

@admin.register(PropertyMedia)
class PropertyMediaAdmin(ImportExportModelAdmin):
    pass