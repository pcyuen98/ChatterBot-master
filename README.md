
#Installation Step

pip install chatterbot

pip install spacy==2.1.0

python -m spacy download en_core_web_sm

python -m spacy link en_core_web_sm en

python manage.py migrate

python manage.py createsuperuser


#Command to Run Server
python manage.py runserver 0.0.0.0:8000
