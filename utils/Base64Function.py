import base64

def Decode(string):
    result=base64.b64decode(string)
    return result

def Encode(string):
    result=base64.b64encode(string)
    return result