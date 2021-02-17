import requests
from bs4 import BeautifulSoup
import os

proxies = {"http": "socks5://127.0.0.1:9050",
          "https": "socks5://127.0.0.1:9050"}

def validacao(url, nome, pasta):
    try:
        if nome not in os.listdir(pasta):
            print("Download ->", pasta+nome)
            return True
    except:
        os.makedirs(pasta)
        print("Download ->", pasta+nome)
        return True
    print("Já existente ->", pasta+nome)
    return False
        
def download_file(url, nome, pasta):
    r = requests.get(url, allow_redirects=True)
    open(pasta+nome, 'wb').write(r.content)

def monta_lista(url):
    r = requests.get(url, proxies=proxies)
    html_doc = r.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    ## pode variar de acordo com o servidor ##
    lista = soup.find_all("a",href=True)
    ##########################################
    return lista

def main(url, pasta):
    lista = monta_lista(url)
    for nome in lista:
        #### pode variar de acordo com o servidor ####
        href = str(nome).split("\"")[1].strip("#")
        new_url = url+"/"+href
        ##############################################
        if "." in href:
            if validacao(url, href, pasta):
                download_file(new_url, href, pasta)
        else:
            main(new_url, pasta+href+"\\")            
            
caminho = os.getcwd()
pasta = caminho+"\\dados\\"
#url = "http://xxx.xxx.xxx.xxx/pasta"
url = input("Insira o endereço <- ")
main(url, pasta)