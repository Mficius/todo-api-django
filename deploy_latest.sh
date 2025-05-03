#!/bin/bash

# === Configuration ===
APP_NAME=todo-api
DOCKER_IMAGE=tonutilisateurdocker/todo-api:latest
APP_PORT=8000
DOMAIN_NAME=example.com
NGINX_CONF_PATH="/etc/nginx/sites-available/$APP_NAME"

echo "[+] Pull de la dernière image Docker..."
docker pull $DOCKER_IMAGE

echo "[+] Suppression de l'ancien conteneur..."
docker stop $APP_NAME || true
docker rm $APP_NAME || true

echo "[+] Lancement du nouveau conteneur..."
docker run -d \
  --name $APP_NAME \
  -p 127.0.0.1:$APP_PORT:8000 \
  --restart always \
  $DOCKER_IMAGE

# === NGINX ===
if [ ! -f "$NGINX_CONF_PATH" ]; then
    echo "[+] Configuration Nginx pour $APP_NAME"
    cat <<EOF > $NGINX_CONF_PATH
server {
    listen 80;
    server_name $DOMAIN_NAME;

    location / {
        proxy_pass http://127.0.0.1:$APP_PORT;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }
}
EOF

    ln -s $NGINX_CONF_PATH /etc/nginx/sites-enabled/
fi

echo "[+] Test de configuration Nginx"
nginx -t && systemctl reload nginx

echo "[✓] Déploiement terminé. Application disponible sur http://$DOMAIN_NAME"
