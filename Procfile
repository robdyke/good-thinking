web: python manage.py migrate && python manage.py collectstatic -c --no-input --settings cms.settings.production && waitress-serve --port=$PORT --threads=6 cms.wsgi:application
