import os
from app import create_app, db
from app.models import User, Note
from flask_migrate import Migrate

app = create_app(os.getenv("FLASK_CONFIG", "development"))
migrate = Migrate(app, db, render_as_batch=True)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Note=Note)

