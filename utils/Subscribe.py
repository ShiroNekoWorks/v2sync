import requests as r
import json as js
import base64

def subscribe(url, name):
    """
    Get the data of subscription
    """
    res = r.get(url)
    if res.status_code == 200:
        return res.text
    else:
        NoteConf = {
            "v": "2",
            "ps": "sub {} is unreachable with code {}".format(name, res.status_code),
            "add": "google.com",
            "port": "443",
            "id": "2661b5f8-8062-34a5-9371-a44313a75b6b",
            "aid": "2",
            "net": "tcp",
            "type": "none",
            "host": "",
            "tls": ""
        }
        VmessLink = 'vmess://' + base64.b64encode(str(NoteConf).replace('\n',''))
        return base64.b64encode(str(VmessLink).replace('\n',''))

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
        SubData += subscribe(url, nick)
    with open('../public/sub', 'wt') as f:
        f.write(SubData)
        f.close()