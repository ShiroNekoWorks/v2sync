from utils.Base64Function import Decode,Encode
from utils.Generate import Generate
from utils.Render import Render
import requests as r
import json as js
import uuid
import random
import string
from pprint import pprint
import os
import shutil

# def config_var_substitute():
    # if('%uuid%' in str(conf)):
    #     newuuid=uuid.uuid1()
    #     conf=str(conf).replace('%uuid%',str(newuuid))
    #     print(newuuid)
    # if('%token%' in str(conf)):
    #     token = ''.join(random.sample(string.ascii_letters + string.digits, 24))
    #     conf=str(conf).replace('%token%',token)
    #     print(token)
    # conf=eval(conf)
    # write_conf=js.dumps(conf,indent=4)
    # print(type(conf))
    # print(conf)
    # pprint(conf)
    # write_config('config.json',write_conf)

def clean_public():
    shutil.rmtree('./public')
    os.mkdir('public')
    with open('./public/.gitkeep','wb') as f:
        f.writelines('')
        f.close

def read_config(file):
    with open(file) as json_file:
        config = js.load(json_file)
    return config

def GetNodeConfig(conf):
    keylist=conf['node'].keys()
    print(keylist)

# def write_config(file,content):
#     with open(file,'wb') as json_file:
#         js.dump(content,json_file)

def create_dictionary(path):
    os.mkdir(path)

def GetSubContent(url):
    content=r.get(url).text
    return(content)

if __name__ == "__main__":
    clean_public()
    conf=read_config('config.json')
    global_conf=conf['global']
    pathlist=global_conf['path'].split('/')
    parent_path='./public'
    for i in pathlist:
        if(i==pathlist[len(pathlist)-1]):
            break
        create_dictionary(parent_path+'/'+i)
        parent_path=parent_path+'/'+i
    filename=pathlist[len(pathlist)-1]
    print(filename)
    GetNodeConfig(conf)


