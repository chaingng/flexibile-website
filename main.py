# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import config

env = Environment(loader=FileSystemLoader('./html/', encoding='utf8'))
t = env.get_template('index.html')

#foods = []
#foods.append({'name':u'ラーメン', 'price':400})
#foods.append({'name':u'焼き飯',   'price':500})
#foods.append({'name':u'天津飯',   'price':600})

html = t.render({
    'title' : config.TITLE
         })
#print 'Content-Type: text/html; charset=utf-8\n'
print html.encode('utf-8')
