#!/usr/bin/python
#coding:utf8
'''
Created on 2016年11月9日

@author: yifei
'''
from app import app
from flask.templating import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Miguel'}
    posts = [
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Susan'},
            'body':'The Avengers movie was so cool!'
        }
             
        ]
    return render_template("index.html",
                           user = user,
                           posts = posts)