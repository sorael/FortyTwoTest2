#!/bin/bash

DATE=$(date +'%Y-%m-%d')

chmod 770 .
python manage.py view_models 2> ${DATE}.dat