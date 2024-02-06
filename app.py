from flask import Flask
from routes.peliculas import peliculas
from routes.peliculas import Usuario
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from flask_login import LoginManager
import os

login_manager = LoginManager()
app = Flask(__name__)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

app.secret_key = "2430"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
if os.environ.get('DATABASE.URI'):
    #bd nube
    app.config['SQLALCHEMY_DATABASE_URI_CLOUD'] = os.environ.get('DATABASE_URI')
else:    
    #bd local
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(peliculas)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)