#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chmod -R ubuntu:ubuntu /data/
echo "
server {
    listen 80;
    listen [::]:80;

    server_name ahmedehabdom.tech;

    location /hbnb_static/ {
    	alias /data/web_static/current;
        index index.html;
    }

    location /redirect_me {
     	return 301 https://ahmedehabdom.tech/hbnb_static/;
    }
" > /etc/nginx/sites-available/default
sudo systemctl restart nginx
