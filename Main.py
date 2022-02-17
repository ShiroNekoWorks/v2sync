from utils.Subscribe import subscribe
import json as js
import os
import shutil
import base64

def clean_public():
    '''
    Clean the public folder before the rendering process
    '''
    shutil.rmtree('./public')
    os.mkdir('public')
    with open('./public/.gitkeep','wb') as f:
        f.writelines('')
        f.close()

def read_config(file):
    '''
    Get config from the file
    '''
    with open(file) as json_file:
        config = js.load(json_file)
    return config

def create_dictionary(path):
    '''
    Create a dictionary from the subscription file
    '''
    os.mkdir(path)

if __name__ == "__main__":
    clean_public()
    # Create the folder from the path
    conf=read_config('config.json')
    global_conf=conf['global']
    pathlist=global_conf['path'].split('/')
    parent_path='./public'
    for i in pathlist:
        if(i==pathlist[len(pathlist)-1]):
            break
        create_dictionary(parent_path+'/'+i)
        parent_path=parent_path+'/'+i
    # Creation completed
    filename=pathlist[len(pathlist)-1]

    # Start getting the data from the subscriptions
    subs=conf['subs']
    SubList = []
    for sub in subs:
        if subs[sub]['type']=='sub':
            SubInfo=subscribe(subs[sub]['link'],subs[sub]['nick'])
            SubList.append(SubInfo)
    # End getting the data from the subscriptions

    # Base64 decoding to get the vmess link
    DecodedList = []
    for i in SubList:
        if SubList.index(i) == len(SubList) - 1:
            Decoded = base64.b64decode(i).decode()  # The last one should not contain a ENTER
        else:
            Decoded = base64.b64decode(i).decode() + '\n'
        DecodedList.append(Decoded)
    # End base64 decoding
    
    # Start combine all the links to a string for encoding
    Combined = ''
    for i in DecodedList:
        Combined += i
    # End combine all the links to a string for encoding

    # Start encoding the string to formal vmess subscription format
    Encoded = base64.b64encode(Combined.encode())
    # End encoding the string to formal vmess subscription format

    # Start writing the data to the file
    with open(conf['global']['path'], 'wb') as f:
        f.write(Encoded)
        f.close()
    # End writing the data to the file

    print('Done!')

