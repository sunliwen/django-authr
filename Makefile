all: develop run

test: 
	@echo "Running Python tests"
	python manage.py test --settings=server.test_settings || exit 1
	@echo ""

develop:
	pip install --upgrade setuptools
	pip install -r requirements.txt
	python manage.py syncdb --noinput

run:
	python manage.py runserver 0.0.0.0:8000

