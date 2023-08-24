from sqlalchemy import Column, Integer, String
from .base import Base

class Album(Base):
    __tablename__ = 'album'

    '''
        Tabla ALBUM
        Columnas: ID , NOMBRE, ARTISTA, AÑO, GENERO
    '''

    id = Column(Integer(), primary_key=True, unique=True)
    nombre = Column(String(25), nullable=False)
    artista = Column(String(30), nullable=False)
    año = Column(Integer(), nullable=False)
    genero = Column(String(20), nullable=False)

    def __str__(self):
        return self.name
