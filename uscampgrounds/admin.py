from django.contrib.gis import admin
from uscampgrounds.models import *

class CampgroundAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'campground_code', 'campground_type', 'phone', 'sites', 'elevation', 'hookups', 'amenities')
    list_filter = ('campground_type',)

admin.site.register(Campground, CampgroundAdmin)
