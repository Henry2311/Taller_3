from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import album
from models import base
from config import credentials

app = Flask(__name__)
CORS(app)

engine = create_engine(credentials.DB_URL)
Session = sessionmaker(engine)

#Sesion a utilizar
session_ = Session()


@app.route('/', methods = ['GET'])
def home():
    '''
        {
            'clave':[{clave : valor}]
        }
    '''
    return jsonify({'Respuesta':'Hola Mundo'})

@app.route('/album', methods = ['POST'])
def create_album():
    try:
        data = request.json 
        nombre = data.get('nombre')
        artista = data.get('artista')
        año = data.get('year')
        genero = data.get('genero')

        new_album = album.Album(nombre=nombre,artista=artista,año=año,genero=genero)

        session_.add(new_album)
        session_.commit()
        return jsonify({'msj':"Album creado agregado correctamente", 'Album creado': data})
    except KeyError:
        print("No se incluyeron los atributos")
        return  jsonify({'error': "No se incluyeron todos los atributos" })

@app.route('/album', methods = ['GET'])
def get_album():
    data = session_.query(album.Album.nombre,
                          album.Album.artista,
                          album.Album.año,
                          album.Album.genero).all()
    response = []
    for d in data:
        response.append({
            'nombre':d.nombre,
            'artista':d.artista,
            'year':d.año,
            'genero':d.genero
        })

    return jsonify(response)

@app.route('/album/<int:id>', methods = ['PUT'])
def update_album(id):
    album_ = session_.query(album.Album).get(id)
    
    if album_ is None:
        return jsonify({'message': 'Album no encontrado'})

    data = request.json
    if 'id' in data:
        return jsonify({'message': 'ID no es un campo actualizable'})

    nombre = data.get('nombre')
    artista = data.get('artista')
    año = data.get('year')
    genero = data.get('genero')

    if nombre:
        album_.nombre = nombre
    
    if artista:
        album_.arista = artista

    if año:
        album_.año = año
    
    if genero:
        album_.genero = genero
    
    session_.commit()

    return jsonify({'message': 'Album actualizado correctamente'})

@app.route('/album/<int:id>', methods = ['DELETE'])
def delete_album(id):
    album_ = session_.query(album.Album).get(id)
    
    if album_ is None:
        return jsonify({'message': 'Album no encontrado'})

    session_.delete(album_)
    session_.commit()

    return jsonify({'message': 'Album eliminado correctamente'}) 

def init_database():
    base.Base.metadata.drop_all(engine)
    base.Base.metadata.create_all(engine)


if __name__ == "__main__":
    #init_database()
    app.run(host = "0.0.0.0", port = 8000, debug=True)