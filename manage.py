import os
from app import create_app, db
from app.models import User, Note

app = create_app(os.getenv("FLASK_CONFIG", "development"))

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Note=Note)
