# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template,request

app = Flask(__name__,static_url_path='')

@app.route('/')
def index():
    return render_template('git.html')

@app.route('/python')
def python():
	return render_template('python.html')


@app.route('/javascript')
def javascript():
	return render_template('javascript.html')


	

