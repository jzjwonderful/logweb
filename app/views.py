#!/usr/bin/env python
# coding=utf-8
from app import app
from flask import request
from flask import render_template


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")



@app.route('/updateLog',methods=['GET','POST'])
def updateLog():
    try:
        data = request.get_json()
        return data
    finally:
        return "{'errormsg':'success'}"
    
   

@app.route('/log.html',methods=['GET'])
def logWeb():
    return "null log data"

def process_data(threadName,delay):
    pass
