from django.contrib.gis import admin
from uscampgrounds.models import *


class CampgroundAdmin(admin.GeoModelAdmin):
    default_lon = -98
    default_lat = 38.5
    default_zoom = 6
    max_zoom = 18
    min_zoom = 6
    map_template = 'gis/admin/openlayers_extralayers.html'

    list_display = ('name', 'campground_code', 'campground_type', 'phone', 'sites', 'elevation', 'hookups', 'amenities')
    list_filter = ('campground_type',)
    search_fields = ('name',)


class CampgroundOSMAdmin(admin.OSMGeoAdmin):
    default_lon = -10909310
    default_lat = 4650301
    default_zoom = 6

    list_display = ('name', 'campground_code', 'campground_type', 'phone', 'sites', 'elevation', 'hookups', 'amenities')
    list_filter = ('campground_type',)
    search_fields = ('name',)


admin.site.register(Campground, CampgroundAdmin)
admin.site.register(Campground, CampgroundOSMAdmin)
