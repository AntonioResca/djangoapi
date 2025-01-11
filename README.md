
# djangoapi


###
### installazione
###

     sudo apt update

     python3 -V

     sudo apt install -y python3-pip python3-venv

     python3 -m venv venv

     source venv/bin/activate

     pip install -r requirements.txt

     cd myproject

     python manage.py makemigrations

     python manage.py migrate

     python manage.py runserver

###
### test
### 

per il test delle api è consigliabile usare un client come postman, insomnia, httpie, chrome devtools, ecc...

se disponibile, per un primo, rapido test si può usare curl:

     curl -X POST http://127.0.0.1:8000/api/my-function/ \
          -H "Content-Type: application/json" \
          -d '{"input": 5}'

se tutto funziona ritorna questo json:

     {"result": 10}
