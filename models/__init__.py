from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here
from models.user import User  # Ensure this line is added
from models.history import History  # Ensure this line is added

def init_db(app):
    db.init_app(app)
