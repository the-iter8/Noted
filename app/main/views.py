from flask import render_template, request, redirect

from .forms import ListForm
from . import main
from .. import db
from ..models import User, Note

@main.route('/', methods = ['GET', 'POST'])
def form_():
    form = ListForm()
    if request.method == 'POST':
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
    elif request.method == 'GET':
        tasklist = [note.title for note in Note.query.all()]
        return render_template('index.html', form=form, tasklist=tasklist)

