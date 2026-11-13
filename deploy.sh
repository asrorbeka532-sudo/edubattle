#!/bin/bash
# ===============================================================
# EduBattle - 1-Click Production VPS Deploy Script
# Ubuntu 20.04 / 22.04 / 24.04 LTS uchun avtomatlashtirilgan sozlash
# ===============================================================

set -e

echo "🚀 EduBattle Production serverini o'rnatish boshlandi..."

# 1. Tizim paketlarini yangilash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git ufw nginx

# 2. Docker va Docker Compose o'rnatish (agar mavjud bo'lmasa)
if ! command -v docker &> /dev/null; then
    echo "📦 Docker o'rnatilmoqda..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    sudo usermod -aG docker $USER
    rm get-docker.sh
fi

# 3. Fayrvoll (Xavfsizlik devori) ni sozlash
echo "🛡️ Xavfsizlik devori sozlanmoqda (Portlar: 22, 80, 443)..."
sudo ufw allow 22/tcp || true
sudo ufw allow 80/tcp || true
sudo ufw allow 443/tcp || true
sudo ufw --force enable || true

# 4. Nginx konfiguratsiyasini ulash
echo "🌐 Nginx konfiguratsiyasi ko'chirilmoqda..."
if [ -f "nginx/edubattle.conf" ]; then
    sudo cp nginx/edubattle.conf /etc/nginx/sites-available/edubattle
    sudo ln -sf /etc/nginx/sites-available/edubattle /etc/nginx/sites-enabled/
    sudo rm -f /etc/nginx/sites-enabled/default
    sudo nginx -t && sudo systemctl restart nginx
fi

# 5. Docker konteynerini ishga tushirish
echo "🐳 Docker konteyneri ishga tushirilmoqda..."
docker compose down || true
docker compose up -d --build

# 6. Har kungi avtomatik zaxira (Cron) ni sozlash (Har kecha 03:00 da)
echo "💾 Avtomatik zaxira (Backup cron) sozlanmoqda..."
(crontab -l 2>/dev/null || true; echo "0 3 * * * docker exec edubattle_server python scripts/backup_db.py >> /var/log/edubattle_backup.log 2>&1") | crontab -

echo ""
echo "==============================================================="
echo "🎉 TABRIKLAYMIZ! EduBattle Production serverida to'liq ishga tushdi!"
echo "📍 Server manzili: http://$(curl -s ifconfig.me)"
echo "⚡ WebSockets, 24/7 doimiy xotira va avtomatik zaxira faol!"
echo "==============================================================="
