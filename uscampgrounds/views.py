from django.contrib.gis.geos import Point
from django.shortcuts import render_to_response
from django.template import RequestContext

from uscampgrounds.models import *

def nearby_campgrounds(request):
    if request.GET.get('lat') and request.GET.get('lon'):
        origin = Point(float(request.GET.get('lon')), float(request.GET.get('lat')))
        camps = Campground.objects.all().distance(origin).order_by('distance')
    else:
        camps = Campground.objects.all().order_by('name')

    try:  # if it's a number, use it.
        retrieve_count = int(request.GET.get('count', 20))
    except ValueError:  # passed us something besides a number, default to something sane
        retrieve_count = 20

    if retrieve_count != -1:  # but if we got -1 give them all
        camps = camps[:retrieve_count]

    return render_to_response('uscampgrounds/nearby.html', {
        'object_list': camps
    }, context_instance=RequestContext(request))
