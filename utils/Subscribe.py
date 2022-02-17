import requests as r
import json as js

def subscribe(url):
    """
    Get the data of subscription
    """
    return r.get(url).text

if __name__ == '__main__':
    with open('../config.json','rt') as f:
        config = f.read()
        f.close()
    config = js.loads(config)
    subs = config['subs']
    subls = []
    for sub in subs:
        if subs[sub]['type'] == 'sub':
            subls.append((subs[sub]['nick'],subs[sub]['link']))
    SubData = ''
    for nick,url in subls:
        SubData += subscribe(url)
    with open('../public/sub', 'wt') as f:
        f.write(SubData)
        f.close()