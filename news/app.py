#/usr/bin/env python3 

from flask import Flask,render_template
import os,json

app=Flask(__name__)


@app.route('/')
def index():


    return render_template("index.html",filename


@app.route('/files/<filename>')
def file(filename):




if __name__=="__main__":
    app.run()


