import datetime
import sys
from optparse import make_option

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from uscampgrounds.load import *


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--path', default='', dest='path',
            help='The directory where the campground data is stored.'),
    )
    help = 'Loads USCampgrounds Data'

    def handle(self, *args, **kwargs):
        base_path = kwargs['path']

        # With DEBUG on this will not work well
        settings.DEBUG = False

        print("Begin: %s" % datetime.datetime.now())

        try:
            import_file = open(os.path.join(base_path, 'NORTHCENTRAL_CAMP.csv'), 'rU')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'NORTHWEST_CAMP.csv'), 'rU')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'SOUTHWEST_CAMP.csv'), 'rU')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'NORTHEAST_CAMP.csv'), 'rU')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'SOUTH_CAMP.csv'), 'rU')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'CALIFORNIA_CAMP.csv'), 'rU')
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'CANADA_CAMP.csv'), 'rU')
        except IOError:
            pass

        print("All Finished: %s" % datetime.datetime.now())
