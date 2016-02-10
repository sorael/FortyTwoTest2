#!/bin/bash

DATE=$(date +'%Y-%m-%d')

chmod go+w .
python manage.py view_models 2> ${DATE}.dat
chmod 700 .