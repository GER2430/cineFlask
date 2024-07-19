from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.pelicula import Pelicula
from utils.db import db
from werkzeug.utils import secure_filename
import os

peliculas = Blueprint('peliculas', __name__)

@peliculas.route("/")
def index():
    peliculas = Pelicula.query.all()
    return render_template('index.html', peliculas=peliculas)

@peliculas.route("/new", methods=['GET'])
def new_movie_page():
    return render_template('new.html')

@peliculas.route("/add", methods=['post'])
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
            filename = secure_filename(imagen.filename)
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
def delete_movie(id):
    pelicula = Pelicula.query.get(id)
    db.session.delete(pelicula)
    db.session.commit()

    flash("pelicula eliminada satisfactoriamente")
    return redirect(url_for('peliculas.index'))

@peliculas.route("/update/<id>", methods = ['POST', 'GET'])
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