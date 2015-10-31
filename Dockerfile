from debian

run apt-get -y update && \
    apt-get -y dist-upgrade && \
    apt-get -y install python-pip git build-essential python-dev mysql-client && \
    apt-get -y clean all
run mkdir /app
run git clone https://github.com/juanifioren/django-oidc-provider.git /app
workdir /app/example_project
copy settings.py /app/example_project/provider_app/settings.py
copy runit.sh /app/runit.sh
run pip install -r requirements.txt
env SITE_URL http://localhost:8080
expose 8080
cmd bash -xe /app/runit.sh
