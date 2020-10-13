##########################################
# This script is for using random proxies#
##########################################

from bs4 import BeautifulSoup as bs
import requests
from random import choice
import pprint as pp

# Get random proxy from www.sslproxies.org
def get_proxy():
    ''' Geting proxy adress and host'''
    url = 'https://www.sslproxies.org/'
    r = requests.get(url)
    soup = bs(r.content, "html5lib")
    return {'https':choice(list(map(lambda x:x[0] + ':' + x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]),
                                                       map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

# Request with random proxy
def proxy_request(request_type, url, **kwargs):
    while 1:
        try:
            proxy = get_proxy()
            print(f'Using proxy: {proxy}')
            r = requests.request(request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except:
            pass
    return r    

# Enter URL for request
r = proxy_request('get',"ENTER URL FOR REQUEST")
pp.pprint(r.text)




