# FOODGRAM


Проект развёрнут и запущен на боевом сервере и доступен по [ссылке]().

Полная документация для API доступна по [ссылке]().

### Описание проекта

Проект создан в рамках учебного курса Яндекс.Практикум.

Cайт Foodgram, «Продуктовый помощник». На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Проект развёрнут и запущен на сервере Yandex.Cloud. Реализованы CI и CD проекта.

### Системные требования

* Python 3.7+
* Docker
* Works on Linux, Windows, macOS


### Стек технологий

* Python 3.7
* Django 3.2.18
* Django Rest Framework
* PostreSQL
* Nginx
* Gunicorn
* Docker
* DockerHub
* GitHub Actions (CI/CD)


### Установка проекта из репозитория

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone

cd
```

2. Cоздать и открыть файл ```.env``` с переменными окружения:
```bash
cd infra

touch .env
```

3. Заполнить ```.env``` файл с переменными окружения по примеру:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgrespassword
DB_HOST=db
DB_PORT=5432
```

4. Запустить приложение в Docker-контейнерах:
```bash
docker-compose up -d --build
```

5. Выполнить миграции, создать суперпользователя, собрать статику, заполнить базу данными:
```bash
docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py createsuperuser

docker-compose exec backend python manage.py collectstatic --no-input

docker-compose exec backend python manage.py load_data
```
