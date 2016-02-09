#!/bin/bash

DATE=`date +%Y-%m-%d`

python manage.py view_models 2> ${DATE}.dat