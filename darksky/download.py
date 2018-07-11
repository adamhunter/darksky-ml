import os
import time
from urllib.request import urlopen
from datetime import datetime

def maybe_download(date: datetime) -> int:
    stamp = str(date).replace(' ', '_')
    cache = 'data/%s.json' % stamp

    if not os.path.exists(cache):
        print('Downloading file...')
        return download(date, cache)
    else:
        size = os.stat(cache).st_size
        print('found {file} with size {size}'.format(file=cache, size=size))
        return size

def download(date: datetime, cache: str) -> int:
    api = os.environ['DARKSKY_API_KEY']
    location = '37.8267,-122.4233' # this is Alcatraz :P silly darksky docs
    epoch = int(time.mktime(date.timetuple()))
    host = 'https://api.darksky.net'
    path = '/forecast/{key}/{loc},{time}?exclude=currently,flags'
    url = host + path.format(key=api, loc=location, time=epoch)

    print('downloading %s' % url)
    try:
        with urlopen(url) as u, open(cache, 'wb') as f:
            return f.write(u.read())
    except:
        print('Exception downloading or saving file %s %s' % url, cache)
        return 0
