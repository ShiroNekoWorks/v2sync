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
        # VmessLink = 'vmess://' + str(base64.b64encode(js.dumps(str(NoteConf).replace('b\'', '').replace('\'', '')).encode()))
        # return base64.b64encode(str(VmessLink).replace('\n', '').replace('b\'', '').replace('\'', '').encode())
        VmessLink = 'vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIlt2MnN5bmMtRVJST1JdVGhpcyBzdWJzY3JpcHRpb24gaXMgY3VycmVudGx5IHVuYXZhbGlhYmxlLCBwbGVhc2UgY2hlY2sgaXQgb3V0ISIsDQogICJhZGQiOiAid3d3LmdpdGh1Yi5jb20iLA0KICAicG9ydCI6ICI0NDMiLA0KICAiaWQiOiAiODhkNjc1M2YtYzA2Ni00OGY1LWE2YzgtYjYzNjQzYTY3OTk0IiwNCiAgImFpZCI6ICI2NCIsDQogICJzY3kiOiAiYXV0byIsDQogICJuZXQiOiAid3MiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAiIiwNCiAgInBhdGgiOiAiL1NoaXJvTmVrb1dvcmtzL3Yyc3luYyIsDQogICJ0bHMiOiAidGxzIiwNCiAgInNuaSI6ICIiDQp9'
        return base64.b64encode(str(VmessLink).encode())
    if res.status_code == 200:
        # print(res.text)
        if res.text == '':
            print('[WARN]No data for {}'.format(name))
            VmessLink = 'vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIlt2MnN5bmMtV0FSTl1UaGlzIHN1YnNjcmlwdGlvbiByZXR1cm5zIGFuIGVtcHR5IHJlc3VsdC4gUGxlYXNlIGNoZWNrIGl0IG91dCEiLA0KICAiYWRkIjogInd3dy5naXRodWIuY29tIiwNCiAgInBvcnQiOiAiNDQzIiwNCiAgImlkIjogIjg4ZDY3NTNmLWMwNjYtNDhmNS1hNmM4LWI2MzY0M2E2Nzk5NCIsDQogICJhaWQiOiAiNjQiLA0KICAic2N5IjogImF1dG8iLA0KICAibmV0IjogIndzIiwNCiAgInR5cGUiOiAibm9uZSIsDQogICJob3N0IjogIiIsDQogICJwYXRoIjogIi9TaGlyb05la29Xb3Jrcy92MnN5bmMiLA0KICAidGxzIjogInRscyIsDQogICJzbmkiOiAiIg0KfQ=='
            return base64.b64encode(str(VmessLink).encode())
        return res.text
    else:
        print('[WARN]The subscription {} is not available, with the status code {}'.format(
            name, res.status_code))
        # NoteConf = {
        #     "v": "2",
        #     "ps": "sub {} is unreachable with code {}".format(name, res.status_code),
        #     "add": "google.com",
        #     "port": "443",
        #     "id": "2661b5f8-8062-34a5-9371-a44313a75b6b",
        #     "aid": "2",
        #     "net": "tcp",
        #     "type": "none",
        #     "host": "",
        #     "tls": ""
        # }
        # VmessLink = 'vmess://' + str(base64.b64encode(str(NoteConf).replace(
        #     '\n', '').replace('b\'', '').replace('\'', '').encode()))
        # return base64.b64encode(str(VmessLink).replace('\n', '').replace('b\'', '').replace('\'', '').encode())
        VmessLink = 'vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIlt2MnN5bmMtRVJST1JdVGhpcyBzdWJzY3JpcHRpb24gaXMgY3VycmVudGx5IHVuYXZhbGlhYmxlLCBwbGVhc2UgY2hlY2sgaXQgb3V0ISIsDQogICJhZGQiOiAid3d3LmdpdGh1Yi5jb20iLA0KICAicG9ydCI6ICI0NDMiLA0KICAiaWQiOiAiODhkNjc1M2YtYzA2Ni00OGY1LWE2YzgtYjYzNjQzYTY3OTk0IiwNCiAgImFpZCI6ICI2NCIsDQogICJzY3kiOiAiYXV0byIsDQogICJuZXQiOiAid3MiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAiIiwNCiAgInBhdGgiOiAiL1NoaXJvTmVrb1dvcmtzL3Yyc3luYyIsDQogICJ0bHMiOiAidGxzIiwNCiAgInNuaSI6ICIiDQp9'
        return base64.b64encode(str(VmessLink).encode())


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
