#!/bin/bash
python ../manage.py reset_db
python ../manage.py flush
python ../manage.py makemigrations uos
python ../manage.py makemigrations profil
python ../manage.py migrate
python ../manage.py runscript create_uos
python ../manage.py runscript create_user