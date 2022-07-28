import random
from logic import *


def main():
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() in ['hi', 'hello', 'start', 'hey']:
                send_message(get_chat_id(update), 'Greetings! Type "Dice" to roll the dice!')
            elif get_message_text(update).lower() == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update), f'You have {_1} and {_2}!\nYour result is {_1+_2}!')
            else:
                send_message(get_chat_id(update), 'Sorry, I can`t understand you')
            update_id += 1


if __name__ == '__main__':
    main()
