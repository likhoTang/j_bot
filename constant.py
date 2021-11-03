import random
from dataclasses import dataclass
from datetime import datetime, date, time

J_BOSS_BOT = '1118680993:AAFojTZPZzRNTUlw5h0nmZb9y0gnJdew3cA'
test_qaz_bot = '1172917753:AAFXBmrXdEHtn7VlEhknWLRHb93b41pGcvk'

POKEMON = '-1001186498703'
MJL = '-1001227180685'

j_words = ['睡了么', '嗯', '明天你来公司吗', '有点着急', '他现在出事了', '晚上一起吃饭不', '在群里说', '都要', '人呢', '有空电话一下', '啊 不着急', '好了', '是什么问题呀',
           '最近很多AL么？', '囧', '请他吃个东西吗', '忙成狗 🐶', '这个要有个提示', '是不是来不及', '今天如果太晚了就明天也可以', '这么奇怪', '活久见', '这么奇怪', '有多少',
           '千万不能有头寸']

sticker_id = "CAACAgEAAxkBAAMRX22mcV21C0VJ90IVtJUlNKBYNkYAAg4BAALWL5sGt11ZS__8bLsbBA"
sticker_id2 = 'CAACAgUAAxkBAAPnX3G_KVrEYzgxVYpslXFsS8g5i5IAAn8BAAKEKxoD99UcDuMUwiAbBA'

# trigger_text_user = ['don', 'evan', 'koma', 'kenny', 'nick', 'ray']
normal_trigger_text = ['ot', '輸', '贏', '波', '加人工', '轉工', '囡', '將軍澳', '屯門', '元朗', '宿舍', '女仔', '安全', '燒嘢食', 'bbq', '師父',
                       'tag', '訓', '大陸', '酒店']

users = [
    {'name': 'don', 'tag': 'Jmcdonaldsw', 'id': '355207143'},
    {'name': 'evan', 'tag': 'evan', 'id': '430454897'},
    {'name': 'kenny', 'tag': 'kennymok1992', 'id': '671267836'},
    {'name': 'nick', 'tag': 'Likho', 'id': '737632365'},
    {'name': 'koma', 'tag': 'komayip', 'id': '545324831'},
    {'name': 'ray', 'tag': 'FatChowChow', 'id': '239786932'},
]


@dataclass
class User:
    name: str
    tag: str
    id: str


# mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"


if __name__ == '__main__':
    print(random.choices(j_words)[0] + random.choices(j_words)[0])
