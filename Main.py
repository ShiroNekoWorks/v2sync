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
    with open('./public/.gitkeep', 'wb') as f:
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
    print('[INFO]Initalizing...')
    clean_public()
    print('[INFO]Initalization Completed!')
    # Create the folder from the path
    print('[INFO]Creating the folder...')
    conf = read_config('config.json')
    global_conf = conf['global']
    pathlist = global_conf['path'].split('/')
    parent_path = './public'
    for i in pathlist:
        if(i == pathlist[len(pathlist)-1]):
            break
        create_dictionary(parent_path+'/'+i)
        parent_path = parent_path+'/'+i
    # Creation completed
    print('[INFO]Created!')
    filename = pathlist[len(pathlist)-1]

    # Start getting the data from the subscriptions
    print('[INFO]Getting the data from the subscriptions...')
    subs = conf['subs']
    SubList = []
    for sub in subs:
        if subs[sub]['type'] == 'sub':
            print('[INFO]Getting the data from the subscription: {}'.format(
                subs[sub]['nick']))
            SubInfo = subscribe(subs[sub]['link'], subs[sub]['nick'])
            print('[INFO]Got the data from the subscription: {}'.format(
                subs[sub]['nick']))
            print('[INFO]Saving the data to the temp: {}'.format(
                subs[sub]['nick']))
            SubList.append(SubInfo)
            print('[INFO]Saved the data to the temp: {}'.format(subs[sub]['nick']))
    # End getting the data from the subscriptions

    # Base64 decoding to get the vmess link
    print('[INFO]Base64 decoding to get the vmess link...')
    DecodedList = []
    for i in SubList:
        if i[:8] == 'vmess://':
            continue
        Decoded = base64.b64decode(i).decode()
        DecodedList.append(Decoded)
    print('[INFO]Base64 decoding completed!')
    # End base64 decoding

    # Start combine all the links to a string for encoding
    print('[INFO]Combining all the links to a string for encoding...')
    Combined = ''
    for i in DecodedList:
        Combined += i.strip()
    print('[INFO]Combined!')
    # End combine all the links to a string for encoding

    # Start encoding the string to formal vmess subscription format
    print('[INFO]Encoding the string to formal vmess subscription format...')
    Encoded = base64.b64encode(Combined.encode())
    print('[INFO]Encoded!')
    # End encoding the string to formal vmess subscription format

    # Start writing the data to the file
    print('[INFO]Writing the data to the file...')
    with open('./public/' + conf['global']['path'], 'wb+') as f:
        f.write(Encoded)
        f.close()
    print('[INFO]Writing completed!')
    # End writing the data to the file

    print('Done!')
