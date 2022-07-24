from os import wait
from flask import render_template, request, redirect, abort, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from .forms import ListForm, LoginForm, RegisterForm
from . import main, auth
from .. import db
from ..models import User, Note

@main.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    form = ListForm()
    if request.method == 'GET':
        tasklist = [note for note in Note.query.filter_by(user_id=current_user.id).all()]
        return render_template('index.html', form=form, tasklist=tasklist)

    elif request.method == 'POST':
        if form.validate_on_submit():
            content = form.content.data
            # TODO: Currently only working for one User.
            # Assign notes to currently logged in User.
            # TODO: separate 'description' form 'title'
            user = User.query.filter_by(name=current_user.name).first()
            note = Note(title=content, description=content, user=user)
            db.session.add(note)
            db.session.commit()
        return redirect(url_for('main.home'))

@main.route('/delete/<int:note_id>', methods = ['GET','POST'])
@login_required
def delete(note_id):
    if request.method == 'GET':
        return abort(404)
    elif request.method == 'POST':
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for('main.home'))

@main.route('/edit/<int:note_id>', methods = ['GET', 'POST'])
@login_required
def edit(note_id):
    if request.method == 'GET':
        return abort(404)
    elif request.method == 'POST':
        note = Note.query.get(note_id)
        note.title = request.form.get("modified_content")
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('main.home'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html',form=form)
    else:
        if form.validate_on_submit():
            new_user_name = form.name.data
            new_user_email_id = form.email_id.data
            new_user_password = form.password.data
            if not User.query.filter_by(email=new_user_email_id).all():
                new_user = User(name=new_user_name, 
                                email=new_user_email_id,
                                password=new_user_password)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('auth.login'))
            flash('Email is already taken.')
            return render_template('register.html',form=form)
        flash("Invalid Credentials")
        return render_template('register.html',form=form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email_id.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.home')
                return redirect(next)
            flash("Invalid Username or password")
            return redirect(url_for('auth.login'))
    else:
        return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
