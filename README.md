# Программа "Интеллектуальный диалог с продвинутым ИИ" с использованием API telegram

Программа нужна для получения ответа от бота на все виды Ваших сообщений. <br />
Сделал студент ___группы ИВТ-101 Рощин Никита___

## Описание

Проект представляет собой простое консольное приложение, которое работает с __API телеграма для ботов:__ __https://api.telegram.org/bot__.

## Установка
Прежде всего для корректной работы кода необходимо установить специальные библиотеки, которые описаны в файле ___"requirements.txt"___ (использовал __requests__ версии __2.31.0__).
Соответственно:
1. Клонируйте репозиторий.
2. Устанавливаете все необходимые библиотеки (см. выше).

## Немного об использованном API
Вызов методов API реализован в виде HTTP запросов на адрес
https://api.telegram.org/bot. 
Параметры запроса передаются методом GET (URL-encoded). <br />
Реализовано через токен моего бота (можете вставить токен своего бота, просто поменяйте значение 
```python
BOT_TOKEN = 'Ваш токен'
```
<br />

Работает цикл, который будет выполняться до достижения максимального количества счётчика (см. код ниже)
```python
counter = 0
MAX_COUNTER = 100

while counter < MAX_COUNTER:
    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        ...логика работы...
    
    time.sleep(1)
    counter += 1
```

## Использование

Запустите файл `main.py` и бот приобретёт "интеллект"  :)

