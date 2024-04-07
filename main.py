import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6954004997:AAF7O9aP9XhQiLQbakGEIjsijrN7gI_xANE'
TEXT_RESPONSE = 'Ого! Ты мне прислал {}!'
MAX_COUNTER = 100
MEDIA_NAMES = {
    'text': 'текст',
    'photo': 'фото',
    'sticker': 'стикер',
    'voice': 'голосовое сообщение',
    'video': 'видео',
    'animation': 'гифку',
    'video_note': 'кружок',
    'document': 'документ'
}

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
            media_types = ['text', 'photo', 'sticker', 'voice', 'video', 'animation', 'video_note', 'document']
            for media_type in media_types:
                if media_type in message:
                    russian_name = MEDIA_NAMES.get(media_type, media_type)
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format(russian_name)}')
                    break

    time.sleep(1)
    counter += 1
