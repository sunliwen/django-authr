all: develop run

develop:
	pip install --upgrade setuptools
	pip install -r requirements.txt
	python manage.py syncdb --noinput

run:
	python manage.py runserver 0.0.0.0:8000

