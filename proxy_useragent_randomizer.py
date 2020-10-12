from fake_useragent import UserAgent
from proxy_requests import ProxyRequests

ua = UserAgent()

page_list = ['https://api.ipify.org/',
             'https://api.ipify.org/?format=json'
            ]

def get_page(page_links, user_agent):
    r = ProxyRequests(link)
    r.set_headers({'User-Agent': user_agent})
    r.get_with_headers()
    return r
    
while True:
    for link in page_list:
        page = get_page(link, ua.random)
        print(page.get_proxy_used())
        print(ua.random)
        print(link)
        print(page)
        print('-' * 15, '\n')