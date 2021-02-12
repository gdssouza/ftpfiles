import requests
from bs4 import BeautifulSoup

url = "https://meuip.co/"
proxy = {"http": "socks5://127.0.0.1:9050",
         "https": "socks5://127.0.0.1:9050"}
r = requests.get(url, proxies=proxy)

html_doc = r.content
soup = BeautifulSoup(html_doc, 'html.parser')

#ingles
meuip = soup.find_all(class_="cf-footer-item sm:block sm:mb-1")[1].get_text()
print(meuip)

#portugues
#meuip = soup.find_all(class_="loading-percent")[0].get_text()
#print(meuip)