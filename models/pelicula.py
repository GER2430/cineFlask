from utils.db import db

class Pelicula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(256), nullable = False)
    director = db.Column(db.String(256), nullable = False)
    genero = db.Column(db.String(256), nullable = False)
    lanzamiento = db.Column(db.Integer, nullable = False)
    duracion = db.Column(db.String(256), nullable = False)
    sinopsis = db.Column(db.Text, nullable = False)
    #imagen = db.Column(db.String(256), nullable = True)

    def __init__(self, titulo, director, genero, 
                 lanzamiento, duracion, sinopsis):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.lanzamiento = lanzamiento
        self.duracion = duracion
        self.sinopsis = sinopsis
        #self.imagen = imagen