# Тестовое задание
В проекте демонстрируется работа с API сервиса https://m3o.com/ с использованием их официальной библиотеки m3o-py

# Установка и проверка

## Схема наполнения файла .env проекта django_stripe
Файл необходимо разместить в директории django_stripe/infra/

```
MO3_TOKEN=*** # Тут должен быть API токен из личного кабинета https://m3o.com/
```

Для запуска проекта необходимо клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:RussianPostman/Test_work_05.03.23.git

```

- для MacOS
```
python3 -m venv venv
source venv/bin/activate
```
- для Windows
```
python -m venv venv
source venv/Scripts/activate
```

Для быстрой проверки функций ввести
```
http://127.0.0.1/admin
```
Для тестирования процесса покупки:
```
python3 main.py
```
