import random
import constant

from telegram import Bot, ParseMode


def format_text(text):
    lines = text.split("\n")
    # todo monospace size
    """ set align to center """
    new_data = []
    sep = " : "
    max_len = max(x.find(sep) for x in lines)
    for x in lines:
        if sep in x:
            space = " " * (max_len - x.find(sep))
            x = space + x
        if "*" not in x:
            x = f"`{x}`"
        new_data.append(x)
    return "\n".join(new_data)


class TgSender:
    buffer = {}

    def __init__(self, token):
        self.bot = Bot(token=token)

    def send(self, text, chat_id):
        return self.bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode="HTML",  # Markdown
        )

    def send_formatted(self, text, chat_id, align=True):
        if align:
            text = f"{format_text(text)}"
        return self.bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=ParseMode.MARKDOWN,
        )

    def update_formatted(self, text, chat_id, message_id, align=True):
        if align:
            text = f"{format_text(text)}"
        return self.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            parse_mode=ParseMode.HTML,
        )

    def send_or_update_formatted(self, text, chat_id, seq, align=True):
        key = f"{chat_id}_{seq}"
        if key not in self.buffer:
            sent_info = self.send_formatted(text, chat_id, align)
            print(sent_info)
            self.buffer[key] = sent_info['message_id']
        else:
            self.update_formatted(text, chat_id, self.buffer[key], align)

    def send_sticker(self, chat_id, sticker_id):
        return self.bot.send_sticker(chat_id, sticker_id)


def get_sender(bot=None):
    if bot:
        return TgSender(bot)
    return TgSender(constant.J_BOSS_BOT)


sender = get_sender()


def send(chat_id, text):
    return sender.send(text, chat_id)


def random_send(chat_id):
    text = random.choices(constant.j_words)[0]
    return sender.send(text, chat_id)


def random_send_with_tag(chat_id, tag):
    text = random.choices(constant.j_words)[0]
    return sender.send(f'@{tag} {text}', chat_id)


def send_sticker(chat_id, sticker_id):
    return sender.send_sticker(chat_id, sticker_id)


def get_user_from_text(text) -> constant.User:
    for user in constant.users:
        if user['name'] in text.lower():
            return constant.User(**user)


def get_mention(user: constant.User):
    mention = f"[{user.name}](tg://user?id={str(user.id)})"
    return mention


if __name__ == '__main__':
    import constant
    sender = TgSender(constant.J_BOSS_BOT)
    print(sender.send(f"[Username](tg://user?id=737632365)",'737632365')) #message`enlight piece`
    # print(sender.update_formatted("code123",'737632365',297))
    # print(sender.send_sticker(constant.POKEMON,constant.sticker_id2)) #sticker
    pass
