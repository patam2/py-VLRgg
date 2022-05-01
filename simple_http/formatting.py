import re
from collections import defaultdict


def get_host(url: str) -> str:
    url = url.split('/', 3)
    if len(url) == 1:
        return url[0]

    if len(url) != 4:
        page = ''
    elif len(url) != 1:
        page = '/' + url[3]

    host = url[2]
    return host

def parse_url(url: str) -> tuple[str, int]:
    page, port = None, 443
    if url.startswith('http:'):
        port = 80
    if url.startswith('https:'):
        port = 443
  
    host = get_host(url)
    

    return host, port

def parse_request_data(data: bytes) -> dict:
    out = defaultdict(str)
    data = data.decode().split('\r\n')

    for i in data:
        if ':' not in i:
            continue
        key, value = i.split(':', 1)
        out[key.lower()] += value
    return out


def get_status_code(data: bytes) -> int:
    return re.search('HTTP/1.1 (\d+)', data.decode().split('\r\n')[0]).group(1)
