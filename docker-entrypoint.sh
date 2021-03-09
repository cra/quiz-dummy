#!/bin/bash

python manage.py migrate

echo 'Starting Gunicorn'
exec gunicorn config.wsgi:application \
	--name quiz-dummy \
	--bind 0.0.0.0:8000 \
	--workers 3\
	--log-level=info \
	"$@"

#python manage.py runserver 0.0.0.0:8000

#touch /srv/logs/gunicorn.log
#touch /srv/logs/access.log
#tail -n 0 -f /srv/logs/*.log &


#echo 'Starting Gunicorn'
#exec gunicorn config.wsgi:application \
	#--name quiz-dummy \
	#--bind 0.0.0.0:8000 \
	#--workers 3\
	#--log-level=info \
	#--log-file=/srv/logs/gunicorn.log \
	#--access-logfile=/srv/logs/access.log \
	#"$@"

