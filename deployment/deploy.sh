#1. apt update (~)
sudo apt-get update

#2. github clone (~)
git clone https://github.com/schooloud/schooloud_back-end.git /home/ubuntu/schooloud_back

#3. install virtual environment (~)
#sudo apt install python3.8-venv
#python -m venv /home/ubuntu/myvenv

#4. activate virtual environment (~)
#source /home/ubuntu/myvenv/bin/activate

#5. set environment variables (~/schooloud_back)
cd /home/ubuntu/schooloud_back
DIR_HOME=$(pwd)
export PYTHONPATH="${PYTHONPATH}:$DIR_HOME"

#6. install from requirements.txt (~/schooloud_back)
 # install pip and zipp
sudo apt install python3-flask
sudo apt install python3-pip
sudo apt-get install python3-zipp
 # pip install
sudo pip install wheel
sudo pip install -r ./requirements.txt # flask script 설치 에러 뜸
 # if flask version error
sudo pip install -U flask
sudo pip install -r ./requirements.txt

#7. install uwsgi and nginx (~/schooloud_back)
sudo apt-get install python3.8-dev
sudo apt-get install nginx
sudo apt-get install uwsgi
sudo apt-get install uwsgi-core
sudo apt-get install uwsgi-plugin-python3

#8. make socket and logs directory (~)
cd /home/ubuntu
mkdir socket
mkdir logs

#9. set uwsgi service (~)
sudo cp /home/ubuntu/schooloud_back/deployment/uwsgi.ini /etc/uwsgi/apps-enabled/schooloud.ini
sudo systemctl enable uwsgi
sudo systemctl restart uwsgi
#if wanna see status of uwsgi service => sudo service uwsgi status

#10. set nginx (~)
sudo cp /home/ubuntu/schooloud_back/deployment/schooloud_app_nginx /etc/nginx/sites-enabled/schooloud
sudo systemctl restart nginx

#11. flask setting (~/schooloud_back/schooloud)
cd /home/ubuntu/schooloud_back/schooloud
flask --app manage db init
flask --app manage db migrate
flask --app manage db upgrade

#12. go to home dir and restart uwsgi(~)
cd /home/ubuntu
sudo systemctl restart uwsgi