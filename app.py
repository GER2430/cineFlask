from flask import Flask
from routes.peliculas import peliculas
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
import os

app = Flask(__name__)

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