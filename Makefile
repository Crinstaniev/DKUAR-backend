dev:
	export FLASK_APP=flaskr
	export FLASK_ENV=development
	flask run

requirements:
	pip freeze > requirements.txt

prod:
	uwsgi --http 127.0.0.1:8000 --master -p 4 -w wsgi:app