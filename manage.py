import os
from app import create_app

print(os.getenv("FLASK_CONFIG", "default"))

app = create_app(os.getenv("FLASK_CONFIG", "default"))
