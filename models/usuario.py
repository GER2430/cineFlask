from utils.db import SQLAlchemy

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(50))

def __init__(self, nombre, correo, password):
    self.nombre = nombre
    self.correo = correo
    self.password_hash = pwd_context.encrypt(password)

def get_id(self):
    return self.id

def is_authenticated(self):
    return True

def is_active(self):
    return True

def is_anonymous(self):
    return False

def check_password(self, password):
        return pwd_context.verify(password, self.password_hash)