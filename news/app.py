#/usr/bin/env python3 

from flask import Flask,render_template
import os,json

app=Flask(__name__)


@app.route('/')
def index():
    filename=[]
    directory=os.path.join(os.getcwd(),"..")
    json_file=[f for f in os.listdir(directory) if ".json" in f]
    for s in json_file:
        filepath=os.path.join(os.getcwd(),"..",s)
        
        with open(filepath) as f:
            data=json.load(f)
            filename.append(data.get("title"))
        
    

    return render_template("index.html",filename=filename)


@app.route('/files/<filename>')
def file(filename):

    pass


if __name__=="__main__":
    app.run()


