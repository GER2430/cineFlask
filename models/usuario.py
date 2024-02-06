from utils.db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120))

    def __init__(self, nombre, username, password):
        self.nombre = nombre
        self.username = username
        self.password_hash = generate_password_hash(password)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)