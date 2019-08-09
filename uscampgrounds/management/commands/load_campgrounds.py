import datetime
import sys
from optparse import make_option

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from uscampgrounds.load import *


class Command(BaseCommand):
    help = 'Loads USCampgrounds Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='The directory where the campground data is stored.')

    def handle(self, *args, **kwargs):
        base_path = kwargs['path']

        # With DEBUG on this will not work well
        settings.DEBUG = False

        print("Begin: %s" % datetime.datetime.now())

        try:
            import_file = open(os.path.join(base_path, 'NortheastCamp.csv'), 'rU', encoding='ISO-8859-1')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'WestCamp.csv'), 'rU', encoding='ISO-8859-1')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'NortheastCamp.csv'), 'rU', encoding='ISO-8859-1')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'SouthCamp.csv'), 'rU', encoding='ISO-8859-1')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'SouthwestCamp.csv'), 'rU', encoding='ISO-8859-1')
            import_info(import_file)
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'MidwestCamp.csv'), 'rU', encoding='ISO-8859-1')
        except IOError:
            pass

        try:
            import_file = open(os.path.join(base_path, 'CanadaCamp.csv'), 'rU', encoding='ISO-8859-1')
        except IOError:
            pass

        print("All Finished: %s" % datetime.datetime.now())
