# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import config

env = Environment(loader=FileSystemLoader('./html/', encoding='utf8'))
t = env.get_template('index.html')

html = t.render({
    'title'  : config.title,
    'maplat' : config.maplat,
    'maplon' : config.maplon,
    'map_info' : config.map_info,
    'footer_on' : False
         })
#print 'Content-Type: text/html; charset=utf-8\n'

f = open('html/test.html','w')
f.write(html.encode('utf-8'))
f.close()