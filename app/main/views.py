from flask import render_template, request, redirect, abort, url_for
from flask_login import login_user

from .forms import ListForm, LoginForm
from . import main, auth
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
        return redirect(url_for('main.home'))

@main.route('/delete/<int:note_id>', methods = ['GET','POST'])
def delete(note_id):
    if request.method == 'GET':
        return abort(404)
    elif request.method == 'POST':
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for('main.home'))

@main.route('/edit/<int:note_id>', methods = ['GET', 'POST'])
def edit(note_id):
    if request.method == 'GET':
        return abort(404)
    elif request.method == 'POST':
        note = Note.query.get(note_id)
        note.title = request.form.get("modified_content")
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('main.home'))

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email_id.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home')
            return redirect(next)
        return "<h1>Invalid Username or password</h1>"
    return render_template('login.html', form=form)
