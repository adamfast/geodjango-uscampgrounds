from django.conf import settings
from django.contrib.gis.db import models

class Campground(models.Model):
    campground_code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    campground_type = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    comments = models.TextField()
    sites = models.CharField(max_length=256)
    elevation = models.CharField(max_length=256)
    hookups = models.CharField(max_length=256)
    amenities = models.TextField()
    point = models.PointField(srid=4326)

    def locator_point(self):
        return self.point

    def __unicode__(self):
        return self.name

# integrate with the django-locator app for easy geo lookups if it's installed
if 'locator.objects' in settings.INSTALLED_APPS:
    from locator.objects.models import create_locator_object
    models.signals.post_save.connect(create_locator_object, sender=Campground)
