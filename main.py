# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import config

env = Environment(loader=FileSystemLoader('./html/', encoding='utf8'))
t = env.get_template('base.html')

html = t.render({
    'title'  : config.title,
    'summary' : config.summary,
    'portfolio' : config.portfolio,
    'top' : config.top,
    'map' : config.map,
    'history' : config.history,
    'contact_location' : config.contact_location,
    'contact_company' : config.contact_company,
    'contact_comment' : config.contact_comment,
    'contact_tel' : config.contact_tel,
    'copyright' : config.copyright,
    'appeal_on' : config.appeal_on,
    'smartphone_on' : config.smartphone_on,
    'contact_on' : config.contact_on,
    'counter_on' : config.counter_on,
    'summary_on' : config.summary_on,
    'review_on' : config.review_on,
    'portfolio_on' : config.portfolio_on,
    'shots_on' : config.shots_on,
    'buyitnow_on' : config.buyitnow_on,
    'map_on' : config.map_on,
    'history_on' : config.history_on,
    'skills_on' : config.skills_on
})

#print 'Content-Type: text/html; charset=utf-8\n'

f = open('html/index.html','w')
f.write(html.encode('utf-8'))
f.close()
