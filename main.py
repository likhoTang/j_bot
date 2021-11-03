from datetime import datetime, time
import random
from time import sleep

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters

import constant
from tg import random_send, random_send_with_tag, TgSender, send_sticker, get_user_from_text, get_mention, send


def i_love_my_boss(update, context):
    chat_id = update.message.chat_id
    print(f'chat_id: {chat_id}')
    if random.randint(0, 9) >= 7:
        resp = send_sticker(chat_id, constant.sticker_id)
    else:
        resp = random_send(chat_id)

    print(resp)


def echo(update, context):
    """Echo the user message."""
    # print(f'{update.message.from_user.first_name}:{update.from_user.id}')
    print(update.message)
    # print(f"From : {update.message.from_user['first_name']} id: {update.message.from_user['id']}")
    update_information = update.message
    chat_id = update_information.chat_id
    user_id = update_information.from_user['id']
    from_user_text = update.message.text.lower()
    print(f'{from_user_text}')

    # tag user
    tag_user = get_user_from_text(from_user_text)
    if tag_user:
        mention = get_mention(tag_user)
        resp = send(chat_id, mention+random.choices(constant.j_words)[0])
        print(resp)

    # normal reply
    elif any(text in from_user_text for text in constant.normal_trigger_text):
        resp = random_send(chat_id)
        print(resp)


    # sleep
    # if time(1, 00, 0) < datetime.now().time() < time(5, 0, 0):
    #     resp = TgSender(constant.J_BOSS_BOT).send('哇 还没睡呀', chat_id)
    #     print(resp)
    #     sleep(60 * 60 * 4)


def main():
    updater = Updater(constant.J_BOSS_BOT, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('i_love_my_boss', i_love_my_boss))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
