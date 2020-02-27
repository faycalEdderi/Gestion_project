#!/bin/bash
python ../manage.py reset_db
python ../manage.py makemigrations
python ../manage.py migrate
python ../manage.py runscript create_database