build:
	docker-compose build landing_page

install-coreui:
	cd landing_page/static/coreui && npm install

run:
	python3 manage.py runserver 0.0.0.0:8000

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

collectstatic:
	python3 manage.py collectstatic --noinput

createadmin:
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'lQ228uqA6Hy6uL4gj1Bj');" | python3 manage.py shell

remove-all-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete
