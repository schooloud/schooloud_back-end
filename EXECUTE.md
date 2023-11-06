# Schooloud 실행 방법
본 문서는 schooloud 서비스 배포 시 설치 후 실행 방법에 대해 기술합니다.<br>
클라우드 인프라 서비스를 위한 서버3대(Backend, proxy, openstack)와 dns 연결을 위한 nhn DNS plus 서비스가 필요합니다.

## 목차
- [Backend-server](#Schooloud-Backend-server)
- [Proxy-server](#Schooloud-Proxy-server)
- [Openstack-server](#Schooloud-Openstack-server)


## Schooloud Backend-server
### 1. git clone
```
git clone https://github.com/schooloud/schooloud_back-end.git
```
### 2. ./deploy.sh 실행
```
./deployment/deploy.sh
```
### 3. 환경변수 설정
```schooloud_back-end/deployment/uwsgi.ini``` 파일의 env를 사용자 환경에 맞게 설정합니다.<br><br>
**※주의※**<br>
서버의 IP주소와 APP_KEY 등 외부에 노출되지 않도록 주의하십시오. <br>
아래의 환경변수가 꼭 포함되어야 합니다.<br>
- PROXY_SERVER=${프록시 서버의 IP 주소}
- OPENSTACK_AUTH_URL=${오픈스택이 설치된 서버에서 오픈스택 인증 주소}
- OPENSTACK_ADMIN_PROJECT=${오픈스택이 설치된 서버에서 관리자 프로젝트 ID}
- APP_KEY=${NHN Cloud Dns plus 서비스 app key}
- FLASK_APP=schooloud
- PYTHONPATH=/home/ubuntu/schooloud_back/schooloud
- SCHOOLOUD_ENV=real <br><br>
아래는 예시 입니다.<br>
```
env=PROXY_SERVER=110.165.16.219
env=FLASK_APP=schooloud
env=PYTHONPATH=/home/ubuntu/schooloud_back/schooloud
env=SCHOOLOUD_ENV=real
env=OPENSTACK_AUTH_URL=http://180.210.81.240/identity
env=OPENSTACK_ADMIN_PROJECT=832d84344c964a78b0c3c1a2d33c3683
```

### 4. 환경변수 적용
```
sudo cp /home/ubuntu/schooloud_back/deployment/schooloud_app_nginx /etc/nginx/sites-enabled/schooloud
sudo systemctl restart uwsgi
```

## Schooloud Proxy-server
### 1. git clone
```
git clone https://github.com/schooloud/schooloud_proxy.git
```
### 2. Flask, nginx 설치
```
sudo apt install flask
sudo apt install nginx
```
### 3. nginx 설정파일 수정
```
sudo vi /etc/nginx/sites-enabled/default
```
아래와 같이 수정합니다.
```
location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri @app;
        }

        location @app {
                include uwsgi_params;
                uwsgi_pass unix:/home/ubuntu/schooloud_proxy/proxy.sock;
        }
```
### 4. uwsgi 실행
```
cd ~/schooloud_proxy
uwsgi --ini proxy.ini
```

## Schooloud Openstack-server
### 1. devstack 설치
다음 [문서](https://openstack.dooray.com/share/pages/cNN00FoxQrSevSxU6RFCpA)를 참조하여 devstack을 설치합니다.

### 2. Wireguard 설정
다음 [문서](https://happyae.tistory.com/84)를 참조하여 proxy 서버와 openstack 서버를 연결합니다.
