# Руководство по запуску проекта Vizitka  API

Это руководство поможет вам настроить и запустить проект на системах Unix и Windows, а также решить некоторые распространённые проблемы, связанные с разными типами переносов строк.

## Требования

- Docker и Docker Compose должны быть установлены.
- Python версии 3.10 или выше.
- Установленная утилита `netcat` (на Unix системах для работы `entrypoint.sh`).
- Для Windows пользователей: убедитесь, что в вашем текстовом редакторе настроены переносы строк в формате `CRLF` для файлов shell (`.sh`).

### Unix-системы

1. **Клонируйте репозиторий**
   ```bash
   git clone <URL_РЕПОЗИТОРИЯ>
   cd VizitkaApi
   ```

2. **Настройка переменных окружения**
   
   Создайте файл `.env` на основе примера `.env.example`:
   ```bash
   cp .env.example .env
   ```
   Заполните файл `.env` необходимыми значениями, такими как `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, а также данными для создания суперпользователя Django.

3. **Запуск с использованием Docker Compose**
   
   Выполните команду для сборки и запуска контейнеров:
   ```bash
   docker-compose -f docker/docker-compose.yml up --build
   ```
   Docker Compose создаст контейнеры для базы данных PostgreSQL, Redis и веб-приложения.

4. **Создание суперпользователя Django**
   
   Суперпользователь создаётся автоматически при запуске, данные для его создания берутся из файла `.env` (переменные `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD`).

5. **Доступ к приложению**
   
   После успешного запуска приложение будет доступно по адресу: [http://localhost:9002](http://localhost:9002).

### Windows-системы

1. **Клонируйте репозиторий**
   
   Откройте командную строку или PowerShell и выполните:
   ```cmd
   git clone <URL_РЕПОЗИТОРИЯ>
   cd VizitkaApi
   ```

2. **Настройка переменных окружения**
   
   Скопируйте файл `.env.example` в `.env` и заполните его данными, как описано выше.

3. **Обратите внимание на формат переносов строк**
   
   Windows использует формат переносов строк `CRLF`, а Unix-системы — `LF`. Чтобы ваш `entrypoint.sh` скрипт заработал на Windows, убедитесь, что он сохранён в формате `CRLF`. Это можно сделать в любом текстовом редакторе, например, в VS Code:
   - Откройте `entrypoint.sh` в VS Code.
   - В нижнем правом углу переключите формат с `LF` на `CRLF`.

4. **Запуск Docker Compose**
   
   Выполните следующую команду в командной строке или PowerShell для запуска контейнеров:
   ```cmd
   docker-compose -f docker\docker-compose.yml up --build
   ```

5. **Доступ к приложению**
   
   После успешного запуска приложение будет доступно по адресу: [http://localhost:9002](http://localhost:9002).

## Проблемы и их решение

1. **Ошибка с подключением к базе данных**
   
   Убедитесь, что база данных PostgreSQL успешно инициализирована и что все переменные в `.env` файле корректно указаны.

2. **Проблема с доступом к скрипту `entrypoint.sh`**
   
   Убедитесь, что файл `entrypoint.sh` имеет права на выполнение. На Unix-системах выполните:
   ```bash
   chmod +x scripts/entrypoint.sh
   ```

3. **Формат переносов строк на Windows**
   
   Если на Windows возникают проблемы с запуском `entrypoint.sh`, убедитесь, что формат файла настроен на `CRLF`, как указано выше.

## Полезные команды Docker

- **Остановка контейнеров**
  ```bash
  docker-compose -f docker/docker-compose.yml down
  ```

- **Перезапуск контейнеров**
  ```bash
  docker-compose -f docker/docker-compose.yml up --build --force-recreate
  ```

- **Просмотр логов**
  ```bash
  docker-compose -f docker/docker-compose.yml logs -f
  ```

## Дополнительно

- **Файл `docker-compose.yml`** используется для локальной разработки, в то время как **`docker-compose.server.yml`** предназначен для развёртывания на сервере.


