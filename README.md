# djangoapi

installazione

sudo apt update

python3 -V

sudo apt install -y python3-pip python3-venv

python3 -m venv venv

source venv/bin/activate

pip install django djangorestframework

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
