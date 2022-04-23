from . import db

class User(db.Model):
    __tablename__ = 'users'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # defines reverse direction of relationship by adding 'user' attribute to Notes.
    # 'user' attribute can be use to access any User from Notes instead of user_id foreign key.
    notes = db.relationship('Note', backref=db.backref('user'))

    def __repr__(self):
        return f"User(id_={self.id_},name={self.name},"\
            f"email={self.email})"

class Note(db.Model):
    __tablename__ = 'notes'
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id_'), nullable=False)

    def __repr__(self):
        return f"Note(id_={self.id_},title={self.title},"\
        f"description={self.description}, user_id={self.user_id})"

