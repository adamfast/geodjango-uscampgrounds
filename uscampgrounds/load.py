import csv
import os
from decimal import Decimal
from django.contrib.gis.geos import Point
from uscampgrounds.models import Campground
from locator.objects.models import *

LON = 0
LAT = 1
CAMPGROUND_CODE = 3
CAMPGROUND_NAME = 4
TYPE = 5
PHONE = 6
COMMENTS = 7
SITES = 8
ELEVATION = 9
HOOKUPS = 10
AMENITIES = 11

def scrub_chars(input):
    input = input.replace('\x96', '')
    input = input.replace('\xa0', '')
    return input

def import_info(import_file):
    reader = csv.reader(import_file, quoting=csv.QUOTE_MINIMAL, delimiter=',')

    for row in reader:
        try:
            camp = Campground.objects.get(campground_code=row[CAMPGROUND_CODE].lower(), campground_type=row[TYPE])
        except Campground.DoesNotExist:
            camp = Campground(campground_code=row[CAMPGROUND_CODE].lower(), campground_type=row[TYPE])

        camp.name = scrub_chars(row[CAMPGROUND_NAME])
        camp.phone = scrub_chars(row[PHONE])
        camp.comments = row[COMMENTS]
        camp.sites = row[SITES]
        camp.elevation = row[ELEVATION]
        camp.hookups = row[HOOKUPS]
        camp.point = Point((Decimal(row[LON]), Decimal(row[LAT])))
        camp.save()


if __name__ == '__main__':
    base_path = '/Users/adam/Downloads/'
    try:
        import_file = open(os.path.join(base_path, 'NORTHCENTRAL.csv'), 'rU')
        import_info(import_file)
    except IOError:
        pass

    try:
        import_file = open(os.path.join(base_path, 'NORTHWEST.csv'), 'rU')
        import_info(import_file)
    except IOError:
        pass

    try:
        import_file = open(os.path.join(base_path, 'SOUTHWEST.csv'), 'rU')
        import_info(import_file)
    except IOError:
        pass

    try:
        import_file = open(os.path.join(base_path, 'NORTHEAST.csv'), 'rU')
        import_info(import_file)
    except IOError:
        pass

    try:
        import_file = open(os.path.join(base_path, 'SOUTH.csv'), 'rU')
        import_info(import_file)
    except IOError:
        pass
