import requests

#target = ' https://docs.hackerone.com/' # Teste de subdominio

target = ' https://WWWWww.hackerone.com'

#try:
#    get_https = requests.get(target)
#    if get_https.status_code == 200:
#        print(f'\033[1;32m{get_https.url} --> status_code 200\033[m')
    
#except:
#    print('Erro desconhecido!')



#print(teste.text)


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
        full = sub + '.' + raw_url
        link_full.append(full)
    return link_full


teste = link_links()

print(teste)

