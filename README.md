## Установка и использование
Проект использует менеджер пакетов poetry
Если у вас его нет то следуйте инструкциям по установке (взято с офф. документации)

- Linux, macOS, Windows (WSL)
Установка poetry
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```
После утсановки необходимо добавить poetry в PATH
- $HOME/.local/bin on Unix.
- %APPDATA%\Python\Scripts on Windows.
- $POETRY_HOME/bin if $POETRY_HOME is set.

В качестве альтернативы, всегда можно использовать полный путь к двоичному файлу poetry:
- ~/Library/Application Support/pypoetry/venv/bin/poetry on MacOS.
- ~/.local/share/pypoetry/venv/bin/poetry on Linux/Unix.
- %APPDATA%\pypoetry\venv\Scripts\poetry on Windows.
- $POETRY_HOME/venv/bin/poetry if $POETRY_HOME is set.

Как только Poetry будет установлена в вашем $PATH, вы можете выполнить следующие действия:
```bash
poetry --version
```
Если у вас высветилась версия poetry - все готово ! Можно переходить к установке проекта и его использованию !

P.S [сайт с документацией на poetry ](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Зависимости проекта
- _python = "^3.10"_
- _poetry = "^version 1.6.1"_

## Environment файл
Проект использует .env файл для хранения SECRET_KEY, DEBUG, database_url(можно добавить для поддержки PostgreSQL для деплоя в будущем), e.g...

Он занесен в гит игнор, но пример содержания и расположения файла есть в репозитории:
- Название файла: .env.example, необходимо его создать как .env в том же месте, где и расположен пример файла, перед запуском приложения


## Установка проекта
```bash
git clone git@github.com:thiSSSnake/test-task-python.git
cd test-task-python/
# установка зависимостей и нужных библиотек
make install
# активация виртуального окружения
poetry shell
# запуск локального сервера
make start
```
## Как пользоваться API
Можно использовать непосредственно браузер или сервис POSTMAN

В данных примерах рассматривается работа с api, с помощью Curl

- _На базовом маршруте '/' ничего не реализованно, просто ссылка на браузерное отображение API.
Все взаимодействия с API происходят с помощью эндпоинтов 'api/v1/'_

- Регистарция нового пользователя:
Для работы с api необходима регистарция и вход(email не обязательный пункт)

```bash
$ curl -X POST http://127.0.0.1:8000/auth/users/ --data 'username=djoser&password=alpine12'
Ответ: {"email": "", "username": "djoser", "id":1}
```
- Вход в систему
```bash
curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'username=djoser&password=alpine12'
Ответ: {"auth_token": токен для авторизации к примеру 09d5712d64aaeb654739272637d5c5fa09be45e9}
```

- Получение списка с данными об объявлениях
```bash
$ curl -H "Authorization: Token 09d5712d64aaeb654739272637d5c5fa09be45e9 http://127.0.0.1:8000/api/v1/ads/
```
- Получение данных объявления по id
```bash
$ curl -H "Authorization: Token 09d5732d64aaeb654739272637d5c5fa09be45e9"  http://127.0.0.1:8000/api/v1/ads/<int:id>/
```
- Выход из системы
```bash
$ curl -X POST http://127.0.0.1:8000/auth/token/logout/ -H "Authorization: Token 09d5732d64aaeb654739272637d5c5fa09be45e9"
```
## DB Migrate
Для миграций можно использовать короткую команду 
```bash
make migrate
```

## Проблема с портом
В рамках тестирования встретил ошибку, что порт 8000 уже используется
исправить ее можно командой:
```bash
sudo fuser -k 8000/tcp
```
Это должно привести к завершению всех процессов, связанных с портом 8000.
