#!/bin/sh
set -e

echo "Начало инициализации базы данных..."

# Подождем некоторое время, чтобы убедиться, что сеть и база данных готовы
echo "Подождем 10 секунд, чтобы убедиться, что сеть и база данных готовы..."
sleep 10

# Ожидание доступности базы данных
echo "Ожидание доступности базы данных..."
until nc -z -v -w30 $POSTGRES_HOST $POSTGRES_PORT
do
  echo "Waiting for PostgreSQL database connection..."
  sleep 1
done

echo "База данных доступна. Создаём миграции..."
python manage.py makemigrations --noinput

echo "Применяем миграции..."
python manage.py migrate --noinput

echo "Собираем статические файлы..."
python manage.py collectstatic --noinput

# echo "Проверяем, были ли уже загружены фикстуры..."
# FIXTURE_FLAG_FILE="fixtures_loaded.flag"

# if [ ! -f $FIXTURE_FLAG_FILE ]; then
#     echo "Фикстуры не загружены. Загружаем фикстуры для каждого приложения..."

#     echo "Загружаем фикстуру пользователей..."
#     python manage.py loaddata apps/users/fixtures/users.json

#     echo "Загружаем фикстуры стран и регионов..."
#     python manage.py loaddata apps/locations/fixtures/countries_and_regions.json
#     python manage.py loaddata apps/locations/fixtures/cities.json

#     echo "Загружаем фикстуры удобств..."
#     python manage.py loaddata apps/amenities/fixtures/amenities.json

#     echo "Загружаем фикстуры типов недвижимости..."
#     python manage.py loaddata apps/properties/fixtures/property_types.json

#     echo "Загружаем фикстуры объектов недвижимости..."
#     python manage.py loaddata apps/properties/fixtures/properties.json

#     # Создаем файл-флаг, чтобы не загружать фикстуры повторно
#     touch $FIXTURE_FLAG_FILE

#     echo "Фикстуры успешно загружены."
# else
#     echo "Фикстуры уже были загружены ранее."
# fi

echo "Создаем суперпользователя, если он не существует..."
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
username = '$DJANGO_SUPERUSER_USERNAME';
password = '$DJANGO_SUPERUSER_PASSWORD';
email = '$DJANGO_SUPERUSER_EMAIL';
if not User.objects.filter(username=username).exists():
    user = User.objects.create_superuser(username=username, password=password, email=email);
    user.is_active = True
    user.save()
    print('Суперпользователь создан и активирован: ' + username);
else:
    print('Суперпользователь уже существует.');
"

# Запускаем переданную команду
exec "$@"
