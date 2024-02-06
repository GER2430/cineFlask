from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from models.usuario import Usuario
from models.pelicula import Pelicula
from utils.db import db
from werkzeug.utils import secure_filename
import os

peliculas = Blueprint('peliculas', __name__)

@peliculas.route("/")
def index():
    if not current_user.is_active:
        return redirect(url_for ('peliculas.login'))
    else:
        peliculas = Pelicula.query.all()
        return render_template('index.html', peliculas=peliculas)

@peliculas.route("/new", methods=['GET'])
@login_required
def new_movie_page():
    return render_template('new.html')

@peliculas.route("/add", methods=['post'])
@login_required
def add_movie():
     if request.method == 'POST':
        titulo = request.form['titulo']
        director = request.form['director']
        genero = request.form['genero']
        lanzamiento = request.form['lanzamiento']
        duracion = request.form['duracion']
        sinopsis = request.form['sinopsis']
        imagen = request.files['imagen']
        if imagen:
            # Asegurarse de que el nombre del archivo sea seguro
            filename = secure_filename(imagen.filename)
            # Guardar la imagen en una ubicación específica (por ejemplo, carpeta "uploads" en el directorio estático)
            ruta_imagen = os.path.join('static/images', filename)
            imagen.save(ruta_imagen)
        
        new_pelicula = Pelicula(titulo, director, genero,
                 lanzamiento, duracion, sinopsis, ruta_imagen)
        
        db.session.add(new_pelicula)
        db.session.commit()

        flash("pelicula añadida satisfactoriamente")

        return redirect(url_for('peliculas.index'))
     else:
        return "Invalid request method"

@peliculas.route("/delete/<id>")
@login_required
def delete_movie(id):
    pelicula = Pelicula.query.get(id)
    db.session.delete(pelicula)
    db.session.commit()

    flash("pelicula eliminada satisfactoriamente")
    return redirect(url_for('peliculas.index'))

@peliculas.route("/update/<id>", methods = ['POST', 'GET'])
@login_required
def update_movie(id):
    pelicula = Pelicula.query.get(id)

    if request.method == 'POST':
        pelicula.titulo = request.form['titulo']
        pelicula.director = request.form['director']
        pelicula.genero = request.form['genero']
        pelicula.lanzamiento = request.form['lanzamiento']
        pelicula.duracion = request.form['duracion']
        pelicula.sinopsis = request.form['sinopsis']

        db.session.commit()

        flash("pelicula actualizada satisfactoriamente")
        return redirect(url_for("peliculas.index"))
    
    return render_template('update.html', pelicula=pelicula)

@peliculas.route("/register", methods = ['GET', 'POST'])
def registro():
    if request.method == "GET":
        return render_template("registro.html")
    elif request.method == "POST":
        nombre = request.form["nombre"]
        username = request.form["username"]
        password = request.form["password"]

        usuario = Usuario(nombre, username, password)
        db.session.add(usuario)
        db.session.commit()

        login_user(usuario)

        return redirect(url_for('peliculas.index'))

@peliculas.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Usuario.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('peliculas.index'))
        else:
            return redirect(url_for('peliculas.login'))
    return render_template('login.html')


@peliculas.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('peliculas.index'))