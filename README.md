# api final yatube

## Описание:

Проект "API для Yatube". В социальной сети Yatube пользователи могут размещать свои публикации. С помощью API можно делать запросы к данным моделей Group, Post, Comment и Follow.

## Как запустить проект:

__Клонировать репозиторий и перейти в него в командной строке:__

```
git clone https://github.com/kochetkov0390/api_final_yatube
```

```
cd api_final_yatube
```

__Cоздать и активировать виртуальное окружение:__

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

__Установить зависимости из файла requirements.txt:__

```
pip install -r requirements.txt
```

__Выполнить миграции:__

```
python3 manage.py migrate
```

__Запустить проект:__

```
python3 manage.py runserver
```
