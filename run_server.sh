#!/bin/sh

DIR_HOME=$(pwd)

export PYTHONPATH="${PYTHONPATH}:$DIR_HOME"

cd schooloud
flask --app manage db migrate
flask --app manage db upgrade