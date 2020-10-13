#######################################################
# This script will download videos, with random proxy #
# -------------Need to change filename and URL--------#
#######################################################

from bs4 import BeautifulSoup as bs
import requests
from random import choice


#Get random proxy
def get_proxy():
    url = 'https://www.sslproxies.org/'
    r = requests.get(url)
    soup = bs(r.content, "html5lib")
    return {'https':choice(list(map(lambda x:x[0] + ':' + x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]),
                                                       map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

Download
def download(request_type, url, **kwargs):
    while 1:
        try:
            chunk_size = 256
            proxy = get_proxy()
            print(f'Using proxy: {proxy}')
            print("Atempt to download.....")
            r = requests.request(request_type, url, proxies=proxy, timeout=5, stream=True, **kwargs)
            with open('NAME.mp4', 'wb') as f:
                for chunk in r.iter_content(chunk_size = chunk_size):
                    f.write(chunk)  
            break
        except:
            pass
    return r    

r = download('get',"INSERT MP4 LINK")
print("Done!!!")




