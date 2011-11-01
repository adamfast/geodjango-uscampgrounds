This app is intended to make storage and import of the data files from http://www.uscampgrounds.info/ - the self-proclaimed "most comprehensive guide to Federal, State, Provincial and Local campgrounds" for your next mashup easy.

Installation instructions:
	- Add 'uscampgrounds' to your INSTALLED_APPS
	- Run a syncdb to get Django to create the necessary database tables for you.
	- Edit uscampgrounds/load.py and set base_path to the directory you downloaded their exports into (downloaded from http://www.uscampgrounds.info/statemaps.html, "Download data files" heading)
	- Export DJANGO_SETTINGS_MODULE for the project you're working on
	- Run python uscampgrounds/load.py and give it a few minutes.
	- Start working with the data!
