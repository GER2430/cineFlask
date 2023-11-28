from flask import Flask
from routes.peliculas import peliculas
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

app = Flask(__name__)

app.secret_key = "2430"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/peliculasdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



app.register_blueprint(peliculas)