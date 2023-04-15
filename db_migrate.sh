#!/bin/bash

source venv/Scripts/activate

flask --app schooloud/manage db migrate
flask --app schooloud/manage db upgrade
