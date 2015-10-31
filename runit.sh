#!/bin/bash -xe

if ! test -e /app/.setup.stamp ; then
  # wait 10 seconds for mysql to show up
  i=0
  while test $i -lt 10 ; do
    if mysql -h $MYSQL_PORT_3306_TCP_ADDR -u $MYSQL_ENV_MYSQL_USER -p $MYSQL_ENV_MYSQL_PASSWORD -P $MYSQL_PORT_3306_TCP_PORT $MYSQL_ENV_MYSQL_DATABASE 'select 1;' ; then
      break
    fi
  done
  python manage.py migrate
  python manage.py creatersakey
  touch /app/.setup.stamp
fi
exec python manage.py runserver 0.0.0.0:8080
