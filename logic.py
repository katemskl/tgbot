import requests

url = "https://api.telegram.org/bot5433575515:AAG6YqunYf0P9yYO329Jm_FAtyi1KoQ3uzs/"


def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat,
              'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
