release: python manage.py migrate; python ./setup.py build_ext --inplace
web: gunicorn config.wsgi --log-file -