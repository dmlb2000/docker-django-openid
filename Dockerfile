from debian

run apt-get -y update && \
    apt-get -y dist-upgrade && \
    apt-get -y install python-pip git build-essential python-dev && \
    apt-get -y clean all
run mkdir /app
run git clone https://github.com/juanifioren/django-oidc-provider.git /app
workdir /app/example_project
run pip install -r requirements.txt
run python manage.py migrate
run python manage.py creatersakey
expose 8080
cmd python manage.py runserver 0.0.0.0:8080
