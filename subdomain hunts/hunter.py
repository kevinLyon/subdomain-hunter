import requests
import sys

#target = ' https://docs.hackerone.com/' # Teste de subdominio

#target = ' https://WWWWww.hackerone.com'


def help():
    print("""

\033[32m         ___           ___           ___                         ___           ___     
        /  /\         /  /\         /  /\          ___          /  /\         /  /\    
       /  /:/        /  /:/        /  /::|        /__/\        /  /::\       /  /::\   
      /  /:/        /  /:/        /  /:|:|        \  \:\      /  /:/\:\     /  /:/\:\  \033[m
\033[35m     /  /::\ ___   /  /:/        /  /:/|:|__       \__\:\    /  /::\ \:\   /  /::\ \:\ 
    /__/:/\:\  /\ /__/:/     /\ /__/:/ |:| /\      /  /::\  /__/:/\:\ \:\ /__/:/\:\_\:\\
    \__\/  \:\/:/ \  \:\    /:/ \__\/  |:|/:/     /  /:/\:\ \  \:\ \:\_\/ \__\/~|::\/:/
        \__\::/   \  \:\  /:/      |  |:/:/     /  /:/__\/  \  \:\ \:\      |  |:|::/ \033[m
\033[36m        /  /:/     \  \:\/:/       |__|::/     /__/:/        \  \:\_\/      |  |:|\/  
       /__/:/       \  \::/        /__/:/      \__\/          \  \:\        |__|:|~   
       \__\/         \__\/         \__\/                       \__\/         \__\|    
\033[m
    """)

    print('\n>> Use: python3 hunter.py -u <site> --wordlist <file path>\n')
    print('         -u               Set Target Ex: [http://domin.site.com] or [teste.com]' )
    print('     --wordlist           Set file path Ex: [--wordlist /Users/user/Desktop/wordlist.txt]' )

def tratamento_de_url(arg):
    lower = arg.lower()
    split = lower.split('.')

    if len(split) == 2:
        return lower 
    elif len(split) > 2:
        del split[0]      
        url_done = split[0] + '.' + split[1]
        return url_done


def tratamento_de_wordlist(arg):
    list = []
    arquivo = open(f"{arg}", "r")
    for txt in arquivo:
        raw = txt.replace('\n', '')
        list.append(raw)
    return list


def link_links(url, wordlist):
    link_full = []
    for sub in wordlist:
        full = str('https://' + sub + '.' + url)
        link_full.append(full)
    return link_full


def argumentos(arg):
    try:
        wordlist = arg.index('--wordlist')
        if wordlist:
            word_raw = tratamento_de_wordlist(arg[wordlist + 1])    
    except:
        pass

    try:
        url = arg.index("-u")
        if url:
            url_raw = tratamento_de_url(arg[url + 1])
    except:
        pass

    try:
        return word_raw, url_raw
    except:
        pass



if __name__ == "__main__":
    argm = sys.argv
    try:
        wordlist, url = argumentos(argm)
        list_urls = link_links(url, wordlist)
   
        for link in list_urls:
            try:
                gets = requests.get(f'{link}')
                print(f'\033[35m\n{gets.url}\033[m \033[32m--> Status code 200\033[m')
            except:
                pass

    except:
        print(help())
        sys.exit(0)



#-----------teste-----------------###


