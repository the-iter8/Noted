from flask import render_template, request, redirect, abort

from .forms import ListForm
from . import main
from .. import db
from ..models import User, Note

@main.route('/', methods = ['GET', 'POST'])
def home():
    form = ListForm()
    if request.method == 'GET':
        tasklist = [note for note in Note.query.all()]
        return render_template('index.html', form=form, tasklist=tasklist)
    elif request.method == 'POST':
        if form.validate_on_submit():
            content = form.content.data
            # TODO: Currently only working for one User.
            # Assign notes to currently logged in User.
            # TODO: separate 'description' form 'title'
            user = User.query.first()
            note = Note(title=content, description=content, user=user)
            db.session.add(note)
            db.session.commit()
            return redirect('/')

@main.route('/delete/<int:note_id>', methods = ['GET','POST'])
def delete(note_id):
    if request.method == 'GET':
        return abort(404)
    elif request.method == 'POST':
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        return redirect('/')

@main.route('/edit/<int:note_id>', methods = ['GET', 'POST'])
def edit(note_id):
    if request.method == 'GET':
        return abort(404)
    elif request.method == 'POST':
        return redirect('/')
