import crawler

WEB = ""
visited = [WEB]
try:
    crawler.crawl(WEB)
except:
    pass
visited = set(visited)
# print(visited)
crawler.write(visited)
# print(len(visited))

import indexer
import time, random
from urllib.parse import urlparse

links = []
host = urlparse(WEB).netloc
hostw = host.replace(".","")
with open("craw_res/"+hostw+".txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        links.append(line[:-1])
# print(links)
reses = []
for link in links:
    if urlparse(link).scheme != "https":
        continue
    print(f"Indexing {link}")
    try:
        time.sleep(random.randint(1,3))
        res = indexer.make_request(link)
        # print(res)
        reses.append(res)
    except KeyboardInterrupt:
        break
    except:
        print(f"Could not get {link}") 

# print(reses)
# reses = ['KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire testname Token: 20', "KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно Goose Gooose goose 🦆🦆🦆🦆🦆🦆🦆 by lox Comments: It's empty, leave first comment now", 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно 123 123 321 by llox Comments: llox - test llox - test - ящм - ZOV', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire rth Token: 34', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback In case you want to make beatiful and formated text 123 by llox goose by llox 1 by testname Lorem ipsum by lox Мудрость дня by lox Goose by lox Lorem ipsum by lox Я лошье by Mes max Филиал Пустоты by lox Write you own post down below', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire denyr Token: 6 Сука блять кто такие фоны делал блять?', "KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно 1 The SSL certificate has been installed! It may take up to 15 minutes for it to become active, АХАХАХАХАХ, а тебе не дали ssl by testname Comments: It's empty, leave first comment now", 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Maxim Token: 15', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Mes max Token: 38', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно goose goose by llox Comments: llox - goose lox - уга-буга', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire lox PABLO denyr rth Gķl Amogus Alenor testname Maxim llox Правитель ĶGE The GBE delegation Andrew Igonin Mes max', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire PABLO Token: 4 гей гей пиздаебанныеблан', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Thanks for visiting KGE | News Welcome back,lox Page Hub Mailbox Your Page', "KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно Мудрость дня Страшно не обосраться - страшно обосраться by lox Comments: It's empty, leave first comment now", 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Current balance: 0 Your token: 1', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire lox Current balance: 0 Token: 1 Ненавижу php. Скоро пойду делать новую игру. Занимаюсь разработкой бэкэнда веб приложений,а так же гей(м)девом. Пипец я тут резюме накатал по сути.', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Наш телеграмм канал Наш дискорд канал Наш гитхаб', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Amogus Token: 9', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback Calculator in HTML CSS & JavaScript AC DEL % / 7 8 9 * 4 5 6 - 1 2 3 + 0 00 . =', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Alenor Token: 10', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Для жироного текста используй |b|, как открытие и |/b|, для закртытия Для курсива текста используй |i|, как открытие и |/i|, для закртытия Для подчеркнутого текста используй |u|, как открытие и |/u|, для закртытия Для зачеркнутого текста используй |b|, как открытие и |/s|, для закртытия Для переноса текста на слeдующую строку используй |nx| Для создания абзацев используй |nx||nx| Обратно', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback Kalkulator Users Igra ot Kamary Forum News Transfer goosinks Goosgle', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback Мини-игра', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Andrew Igonin Token: 36 Люблю биологию', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire The GBE delegation Token: 37', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно Филиал Пустоты Уга-буга by lox Comments: lox - Goose lox - 111', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire llox Token: 18 Goose. FOR THE KGE!!!', "KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно Я лошье Я лошье by Mes max Comments: It's empty, leave first comment now", 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire SEND']

eee = []
for i in range(len(links)):
    text = reses[i]
    text = text.split()
    text = map(indexer.make_ok, text)
    text = [x for x in text if x is not None]
    # text = " ".join(text)
    for j in text:
        eee.append({j:[links[i]]})
# print(eee)

print("Updating")
# update(reses[10],links[10])
# update(reses[13],links[13])
merged_dict = {}

for d in eee:
    for word, urls in d.items():
        if word not in merged_dict:
            merged_dict[word] = []
        
        # Добавляем только новые URL
        for url in urls:
            if url not in merged_dict[word]:
                merged_dict[word].append(url)
# print(merged_dict)
indexer.update(merged_dict)
# alles = len(reses)

print(f"{WEB} Was added to goosgle")