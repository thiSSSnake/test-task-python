install:
	poetry install

start:
	python3 manage.py runserver

lint:
	poetry run flake8 test_task_python

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
