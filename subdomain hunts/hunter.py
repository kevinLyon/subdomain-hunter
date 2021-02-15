import requests
import sys

#target = ' https://docs.hackerone.com/' # Teste de subdominio

target = ' https://WWWWww.hackerone.com'


def tratamento_de_url():
    teste = target.lower()
    teste1 = teste.split('.')
    url_done = teste1[1] + '.' + teste1[2]
    #print(url_done)
    return url_done


def tratamento_de_wordlist():
    list = []
    arquivo = open("subdomain hunts/wordlist.txt", "r")
    for txt in arquivo:
        raw = txt.replace('\n', '')
        list.append(raw)
    return list


def link_links():
    raw_url = tratamento_de_url()
    list = tratamento_de_wordlist()

    link_full = []
    for sub in list:
        full = str('https://' + sub + '.' + raw_url)
        link_full.append(full)
    return link_full



#if __name__ == "__main__":
#
 #   urls = link_links()
#
#    for url in urls:
#        try:
#            gets = requests.get(f'{url}')
#            print(f'\033[35m\n{gets.url}\033[m \033[32m--> Status code 200\033[m')
#        except:
#            pass
