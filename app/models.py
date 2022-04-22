from . import db

class User(db.Model):
    __tablename__ = 'user'
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"User(id_={self.id_},name={self.name},email={self.email})"

class Notes(db.Model):
    __tablename__ = 'note'
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
