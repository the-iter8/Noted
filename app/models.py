from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    # defines reverse direction of relationship by adding 'user' attribute to Notes.
    # 'user' attribute can be use to access any User from Notes instead of user_id foreign key.
    notes = db.relationship('Note', backref=db.backref('user'))

    # password getter
    @property
    def password(self):
        return AttributeError("password is not a readable attribute")

    # password setter 
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # Verifies password
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User(id={self.id},name={self.name},"\
            f"email={self.email})"

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Note(id={self.id},title={self.title},"\
        f"description={self.description}, user_id={self.user_id})"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

