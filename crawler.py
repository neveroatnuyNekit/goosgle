import httpx
import urllib3
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time, random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

WEB = "https://orteil.dashnet.org/"
visited = [WEB]

def write(links):
    host = urlparse(WEB).netloc
    hostw = host.replace(".","")
    with open("craw_res/"+hostw+".txt", "w") as file:
        for link in links:
            try:
                file.write(link)
                file.write("\n")
            except UnicodeEncodeError:
                continue

def crawl(web_site):
    global visited
    # print(visited)
    print(f"{web_site} is crawling")
    time.sleep(random.randint(1,3))
    links = make_request(web_site)
    for link in links:
        if link in visited:
            continue
        if urlparse(link).netloc != urlparse(WEB).netloc or urlparse(link).scheme != "https":
            continue
        visited.append(link)
        crawl(link)
    # return links

def get_links(html,url):
    soup = BeautifulSoup(html, 'html.parser')
        
        # Находим все теги <a> с атрибутом href
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Преобразуем относительные ссылки в абсолютные
        absolute_url = urljoin(url, href)
        if not absolute_url in links:
            links.append(absolute_url)
    return links


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
        return get_links(response.text, url)
    
if __name__ == "__main__":
    try:
        crawl(WEB)
    except:
        pass
    visited = set(visited)
    print(visited)
    write(visited)
    print(len(visited))
