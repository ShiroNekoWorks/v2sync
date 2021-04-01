def Generate(path,content):
    with open('./public/{}'.format(path),'wb') as f:
        f.writelines(content)
        f.close