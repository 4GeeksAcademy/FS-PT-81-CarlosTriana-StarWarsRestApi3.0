"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Favorites, Peoples, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#LOS METODOS A CONTINUACIÓN SON LOS 'GET'

@app.route('/favorites', methods=['GET'])
def all_favorites():
    data = Favorites.query.all()
    data = [favorite.serialize() for favorite in data]
    return jsonify({"msg": "OK", "data": data})

@app.route('/favorite/<int:id>', methods=['GET'])
def one_favorite(id):
    favorite = Favorites.query.get(id)
    print('favorite', favorite)
    return jsonify({"msg": "one favorite with id:" + str(id), "favorite": favorite.serialize()})


@app.route('/users', methods=['GET'])
def all_users():
    data = Users.query.all()
    data = [user.serialize() for user in data]
    return jsonify({"msg": "OK", "data": data})

@app.route('/user/<int:id>', methods=['GET'])
def one_user(id):
    user = Users.query.get(id)
    print('user', user)
    return jsonify({"msg": "one user with id:" + str(id), "user": user.serialize()})


@app.route('/peoples', methods=['GET'])
def all_peoples():
    data = Peoples.query.all()
    data = [people.serialize() for people in data]
    return jsonify({"msg": "OK", "data": data})

@app.route('/people/<int:id>', methods=['GET'])
def one_people(id):
    people = Peoples.query.get(id)
    print('people', people)
    return jsonify({"msg": "one people with id:" + str(id), "people": people.serialize()})


@app.route('/planets', methods=['GET'])
def all_planets():
    data = Planets.query.all()
    data = [planet.serialize() for planet in data]
    return jsonify({"msg": "OK", "data": data})

@app.route('/planet/<int:id>', methods=['GET'])
def one_planet(id):
    planet = Planets.query.get(id)
    print('planet', planet)
    return jsonify({"msg": "one planet with id:" + str(id), "planet": planet.serialize()})


#LOS METODOS A CONTINUACIÓN SON LOS 'POST'

@app.route('/favorites/people', methods=['POST'])
def add_peoples_favorites():
    try:
        people = request.json.get('people', None)
        gender = request.json.get('gender', None)
        if not people or not gender:
            return jsonify({"msg": 'necesitamos el nombre y genero de la persona'}), 400
        check = Favorites.query.filter_by(people=people).first()
        if check:
            return jsonify({"msg": 'la persona ya está en favoritos, inicie sesión'}), 400
        new_favorite = Favorites(people=people, gender=gender)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"msg": "OK", "data": new_favorite.serialize()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error al agregar favorito: {str(e)}"}), 500
    

@app.route('/favorites/planet', methods=['POST'])
def add_planets_favorites():
    try:
        planet = request.json.get('planet', None)
        if not planet:
            return jsonify({"msg": 'necesitamos el nombre del planeta'}), 400
        check = Favorites.query.filter_by(planet=planet).first()
        if check:
            return jsonify({"msg": 'el planeta ya está en favoritos, inicie sesión'}), 400
        new_favorite = Favorites(planet=planet)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"msg": "OK", "data": new_favorite.serialize()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error al agregar favorito: {str(e)}"}), 500


#LOS METODOS A CONTINUACIÓN SON LOS 'DELETE'

@app.route('/favorites/peoples/<int:id>', methods=['DELETE'])
def delete_people_favorite(id):
    favorite = Favorites.query.filter_by(id=id).first()
    if favorite:
        try:
            db.session.delete(favorite)
            db.session.commit()
            return jsonify({"msg": f"Se eliminó a la persona con id: {id} de favoritos"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"msg": "Se produjo un error al eliminar a la persona de favoritos", "error": str(e)}), 500
    else:
        return jsonify({"msg": f"Persona con id: {id} no encontrada en favoritos"}), 404
    

@app.route('/favorites/planets/<int:id>', methods=['DELETE'])
def delete_planet_favorite(id):
    favorite = Favorites.query.filter_by(id=id).first()
    if favorite:
        try:
            db.session.delete(favorite)
            db.session.commit()
            return jsonify({"msg": f"Se eliminó a el planeta con id: {id} de favoritos"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"msg": "Se produjo un error al eliminar el planeta de favoritos", "error": str(e)}), 500
    else:
        return jsonify({"msg": f"Planeta con id: {id} no encontrada en favoritos"}), 404




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
