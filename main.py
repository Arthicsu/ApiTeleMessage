import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6954004997:AAF7O9aP9XhQiLQbakGEIjsijrN7gI_xANE'
TEXT_RESPONSE = 'Ого! Ты мне прислал {}!'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id = None

while counter < MAX_COUNTER:
    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            message = result['message']
            if 'text' in message:
                text = message['text']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("Текст")}')
            elif 'photo' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("Фотка")}')
            elif 'sticker' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("Стикер")}')
            elif 'voice' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("Голосовое сообщение")}')
            elif 'video' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("Видео")}')
            elif 'animation' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("Гифка")}')
            elif 'video_note' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("Кружок")}')
            elif 'document' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("Какой-то документ")}')

    time.sleep(1)
    counter += 1