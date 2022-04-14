from flask import render_template, request, redirect
from . import main


@main.route('/', methods = ['GET', 'POST'])
def form():
    f = open("test.txt","a+")
    if request.method == 'POST':
        content = request.form['content']
        try:
            f.write(content + "\n")
            return redirect('/')
        except:
            return "There was an issue adding the text. "

    else:
        f = open("test.txt","r")
        tasklist = f.readlines()
        
        return render_template("index.html", tasklist = tasklist)

