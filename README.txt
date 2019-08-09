This app is intended to make storage and import of the data files from http://www.uscampgrounds.info/ - the self-proclaimed "most comprehensive guide to Federal, State, Provincial and Local campgrounds" to make your next mashup easier.

Installation instructions:
	- Add 'uscampgrounds' to settings.INSTALLED_APPS
	- `python manage.py migrate` to ask Django to create the necessary database tables for you.
	- `python manage.py load_campgrounds --path=/PATH/TO/USCAMPGROUNDS/CSVS/` and give it a few minutes.
	- Start working with the data and having fun!
