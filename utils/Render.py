import jinja2

def Render(tamplate_name,path,path_enable):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('../tamplate/{}'.format(tamplate_name)))
    tamplate=env.get_template('../tamplates/{}'.format(tamplate_name),path_enable=path_enable,path=path)
    render_result=tamplate.render(path=path)
    with open('../public/index.html','wb') as f:
        f.writelines(render_result)
        f.close()