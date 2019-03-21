from flask import Flask,render_template,request,jsonify
#from wtforms import TextField
from source import inpo,clear
import subprocess
import os, sys
from subprocess import check_output
import time
import json
#files to import
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/background_process')
def background_process():
    try:
        inp = request.args.get('proglang', type=str)#input from "convert" html page
        inpo(inp)#passing to writing the input file for text x
        #lang=int(lang)
        #res=red.test.Fibonacci(lang)
        process()#function for subprocess of pseudo code .tx
        text=open('output.txt','r+')
        res=text.read()
        text.close()
        return jsonify(result=res)#for dynamic output
    except Exception as e:
        return str(e)

def process():
    subprocess.call(['python.exe','pseudo.py',],#calling subprocess for running programs
    stdout=open('output.txt','wb'))

@app.route('/convertor',methods=['GET','POST'])
def convertor():
    return render_template('display.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404#error handler for incorrect pages

if __name__ == '__main__':
    app.run(debug=True)
