import requests
from bs4 import BeautifulSoup
import os

proxy = {"http": "socks5://127.0.0.1:9050",
         "https": "socks5://127.0.0.1:9050"}

def download_file(url, nome, pasta):
    r = requests.get(url, allow_redirects=True)
    try:
        open(pasta+nome, 'wb').write(r.content)
    except:
        os.makedirs(pasta)
        open(pasta+nome, 'wb').write(r.content)

def monta_lista(url, proxy=proxy):
    r = requests.get(url, proxies=proxy)
    html_doc = r.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    lista = soup.find_all("a",href=True)
    return lista

def main(url, pasta):
    lista = monta_lista(url)
    for nome in lista[1:]:
        nome = nome.get_text()
        new_url = url+"/"+nome
        if "." in nome:
            download_file(new_url, nome, pasta)
            print("Download ->", new_url)
        else:
            main(new_url, pasta+nome+"\\")            
            
#url = "http://xxx.xxx.xxx.xxx/pasta"
caminho = os.getcwd()
pasta = caminho+"\\dados\\"
url = input("Insira o endereço <- ")
main(url, pasta)