import requests as r
from requests import ConnectionError
import json as js
import base64


def subscribe(url, name):
    """
    Get the data of subscription
    """
    try:
        res = r.get(url, timeout=30)
    except ConnectionError:
        print('[ERROR]Connection timeout for {}'.format(name))
        # NoteConf = {
        #     "v": "2",
        #     "ps": "sub {} is unavaliable because of network timeout".format(name, res.status_code),
        #     "add": "google.com",
        #     "port": "443",
        #     "id": "2661b5f8-8062-34a5-9371-a44313a75b6b",
        #     "aid": "2",
        #     "net": "tcp",
        #     "type": "none",
        #     "host": "",
        #     "tls": ""
        # }
        # print(js.dumps(str(NoteConf)))
        # VmessLink = 'vmess://' + str(base64.b64encode(js.dumps(str(NoteConf).replace(
        #     '\n', '').replace('b\'', '').replace('\'', '')).encode()))
        # return base64.b64encode(str(VmessLink).replace('\n', '').replace('b\'', '').replace('\'', '').encode())
        VmessLink = 'vmess://' + 'eyJ2IjoiMiIsInBzIjoiVGhpcyBzdWIgaXMgdW5hdmFsaWFibGUsIHBsZWFzZSBjaGVjayBpdCBvdXQhIiwiYWRkIjoid3d3LmcwMGdsZS5jb20iLCJwb3J0IjoiMTAwODYiLCJpZCI6IjI2MTIzM2Y4LTgwNjItMzRhNS05MzcxLWE0NDMzMzMzMzM2YiIsImFpZCI6IjIiLCJuZXQiOiJ0Y3AiLCJ0eXBlIjoibm9uZSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==\n'
        return base64.b64encode(str(VmessLink).encode())
    if res.status_code == 200:
        return res.text
    else:
        print('[WARN]The subscription {} is not available, with the status code {}'.format(name, res.status_code))
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
        VmessLink = 'vmess://' + str(base64.b64encode(str(NoteConf).replace(
            '\n', '').replace('b\'', '').replace('\'', '').encode()))
        return base64.b64encode(str(VmessLink).replace('\n', '').replace('b\'', '').replace('\'', '').encode())


if __name__ == '__main__':
    '''
    Code for debug, also for single subscription
    '''
    with open('../config.json', 'rt') as f:
        config = f.read()
        f.close()
    config = js.loads(config)
    subs = config['subs']
    subls = []
    for sub in subs:
        if subs[sub]['type'] == 'sub':
            subls.append((subs[sub]['nick'], subs[sub]['link']))
    SubData = ''
    for nick, url in subls:
        SubData += subscribe(url, nick)
    with open('../public/sub', 'wt') as f:
        f.write(SubData)
        f.close()
