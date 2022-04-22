from flask import render_template, request, redirect

from .forms import ListForm
from . import main

@main.route('/', methods = ['GET', 'POST'])
def form_():
    form = ListForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            with open("test.txt", "a+") as f:
                content = form.content.data
                f.write(content + '\n')
                return redirect('/')
    elif request.method == 'GET':
        f = open("test.txt", "r")
        tasklist = f.readlines()
        print(form.content())
        print(form.submit())
        return render_template('index.html', form=form, tasklist=tasklist)

