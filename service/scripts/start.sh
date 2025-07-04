#!/bin/bash
set -e

while ! nc -z db 5432; do
  echo "🟡 Aguardando iniciar container do Banco de Dados Postgres(db 5432) ..."
  sleep 2
done

echo "✅ Container do Banco de Dados Postgres iniciado com sucesso! (db:5432)"

python src/manage.py collectstatic --noinput

echo "🟡 Migrando o banco de dados..."
python src/manage.py makemigrations
python src/manage.py migrate --noinput
echo "✅ Banco de dados migrado com sucesso!"

python src/manage.py shell -c "
from authentication.models import Profile;
if not Profile.objects.filter(username='admin').exists():
    Profile.objects.create_superuser(username='admin', email='admin@example.com', password='123', profileType=1)
"

# gunicorn plantagora.wsgi:application --bind 0.0.0.0:8001 --chdir src
# python src/manage.py runserver 0.0.0.0:8001
uvicorn src.plantagora.asgi:application --host 0.0.0.0 --port 8001 --reload --workers 4
