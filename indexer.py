import httpx
import urllib3
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time, random, json, re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from collections import defaultdict


WEB = "https://orteil.dashnet.org/"
# visited = [WEB]

GET_OUT = {
    "for",
    "you",
    "this",
    "more",
    "without",
    "may",
    "through",
    "between",
    "after",
    "before",
    "thanks",
    "your",
}


def get_text(html):
    # soup = BeautifulSoup(html, 'html.parser')
        
    #     # Находим все теги <a> с атрибутом href
    # links = []
    # for link in soup.find_all('a', href=True):
    #     href = link['href']
    #     # Преобразуем относительные ссылки в абсолютные
    #     absolute_url = urljoin(url, href)
    #     if not absolute_url in links:
    #         links.append(absolute_url)
    # return links
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style", "noscript", "meta", "link"]):
        script.decompose()  # Удаляем ненужные теги

    text = soup.get_text(separator=' ', strip=True)
    return text


def make_request(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json",  # например, если API требует JSON
    }

    if urlparse(url).netloc == "kringege.free.nf":

        from Crypto.Cipher import AES
        from Crypto.Util.Padding import unpad

        # Данные из JS
        key = bytes.fromhex("f655ba9d09a112d4968c63579db590b4")
        iv = bytes.fromhex("98344c2eee86c3994890592585b49f80")
        encrypted_data = bytes.fromhex("88a6f2989e25ac9cb86fa3c920a18c9e")

        # Расшифровка AES-256-CBC
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted_data)
        cookie_value = decrypted.hex()  # Кука __test

        # Отправляем запрос с кукой
        cookies = {"__test": cookie_value, "PHPSESSID":"7c3993060fe47d27b0cf58bd94722cc5"}
    else:
        cookies = {}

    with httpx.Client(
        headers=headers,
        http2=True,  # если нужен HTTP/2
        verify=False,  # отключение SSL-проверки
        cookies=cookies,
        follow_redirects=True,
    ) as client:
        response = client.get(url)
        # print(response.text)
        # print(get_links(response.text, url))
        # return get_links(response.text, url)
        return get_text(response.text)

# print(make_request(WEB))

def load(file):
    with open(file, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            return {}
    return(data)


def write(file,data):
    with open(file, "w", encoding="utf-8") as file:
        # new_data = {"123":113,"ww":[12,21,"21"],112:{"123":321}}
        new_data = data
        file.write(json.dumps(new_data,ensure_ascii=False,))

def make_ok(text:str):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    if len(text) <= 2 or text in GET_OUT:
        return None
    if text:
        return text
    return None

def update(b):
    a = load("indexes.json")


    merged_dict={}

    for key in a.keys() | b.keys():
        merged_urls = list(set(a.get(key, []) + b.get(key, [])))
        merged_dict[key] = merged_urls

    c = dict(merged_dict)
    # print(c)
    write("indexes.json",c)

if __name__ == "__main__":
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
            time.sleep(random.random()*2)
            res = make_request(link)
            # print(res)
            reses.append(res)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Could not get {link}: {e}") 

    # print(reses)
    # reses = ['KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire testname Token: 20', "KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно Goose Gooose goose 🦆🦆🦆🦆🦆🦆🦆 by lox Comments: It's empty, leave first comment now", 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно 123 123 321 by llox Comments: llox - test llox - test - ящм - ZOV', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire rth Token: 34', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback In case you want to make beatiful and formated text 123 by llox goose by llox 1 by testname Lorem ipsum by lox Мудрость дня by lox Goose by lox Lorem ipsum by lox Я лошье by Mes max Филиал Пустоты by lox Write you own post down below', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire denyr Token: 6 Сука блять кто такие фоны делал блять?', "KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно 1 The SSL certificate has been installed! It may take up to 15 minutes for it to become active, АХАХАХАХАХ, а тебе не дали ssl by testname Comments: It's empty, leave first comment now", 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Maxim Token: 15', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Mes max Token: 38', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно goose goose by llox Comments: llox - goose lox - уга-буга', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire lox PABLO denyr rth Gķl Amogus Alenor testname Maxim llox Правитель ĶGE The GBE delegation Andrew Igonin Mes max', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire PABLO Token: 4 гей гей пиздаебанныеблан', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Thanks for visiting KGE | News Welcome back,lox Page Hub Mailbox Your Page', "KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно Мудрость дня Страшно не обосраться - страшно обосраться by lox Comments: It's empty, leave first comment now", 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Current balance: 0 Your token: 1', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire lox Current balance: 0 Token: 1 Ненавижу php. Скоро пойду делать новую игру. Занимаюсь разработкой бэкэнда веб приложений,а так же гей(м)девом. Пипец я тут резюме накатал по сути.', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Наш телеграмм канал Наш дискорд канал Наш гитхаб', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Amogus Token: 9', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback Calculator in HTML CSS & JavaScript AC DEL % / 7 8 9 * 4 5 6 - 1 2 3 + 0 00 . =', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Alenor Token: 10', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Для жироного текста используй |b|, как открытие и |/b|, для закртытия Для курсива текста используй |i|, как открытие и |/i|, для закртытия Для подчеркнутого текста используй |u|, как открытие и |/u|, для закртытия Для зачеркнутого текста используй |b|, как открытие и |/s|, для закртытия Для переноса текста на слeдующую строку используй |nx| Для создания абзацев используй |nx||nx| Обратно', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback Kalkulator Users Igra ot Kamary Forum News Transfer goosinks Goosgle', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback Мини-игра', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Andrew Igonin Token: 36 Люблю биологию', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire The GBE delegation Token: 37', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно Филиал Пустоты Уга-буга by lox Comments: lox - Goose lox - 111', 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire llox Token: 18 Goose. FOR THE KGE!!!', "KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire Обратно Я лошье Я лошье by Mes max Comments: It's empty, leave first comment now", 'KGE - Kringe Goose Empire Kringe Goose Empire Главная Контакты Хаб - - - Leave feedback KGE - Kringe Goose Empire SEND']

    eee = []
    for i in range(len(links)):
        text = reses[i]
        text = text.split()
        text = map(make_ok, text)
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
    update(merged_dict)
    alles = len(reses)