# API utilizando FLASK y SQLALCHEMY

Ejemplo de uso de la librería Flask para la creación de un API server
Se utiliza la libreria SQLALCHEMY para realizar la conexión con la Base de datos en MYSQL

## Instalación

Para la instalacion de Flask utilizar el siguiente comando

```bash
pip install Flask Flask-CORS
```
Para la instalacion de SQLAlChemy utilizar el siguiente comando

```bash
pip install SQLAlchemy
```
### Librerias extra
Instalar los drivers para el uso de la Base de datos, este puede variar segun la Base de datos a utilizar en este caso es MySQL

```bash
pip install mysql-connector-python
```

## Documentacion 
Para conocer más a detalle las librerias pueden constultar los enlaces:
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Tutorial](https://drive.google.com/file/d/1MqNL0aAwjDyo2LxqZFnKVtuKSSOROyZm/view?usp=sharing)


## Comandos Docker

```bash
sudo docker images
sudo docker ps 
sudo docker ps -a
sudo docker run --name devmysql -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 -d mysql:latest
sudo docker exec devmysql mysql -uroot -p
```
