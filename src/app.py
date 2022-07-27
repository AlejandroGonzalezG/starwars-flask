from flask import Flask, jsonify, request, json
from flask_migrate import Migrate
from models import db, User, Character, Planet, Film, Specie, Vehicle, Starship, Favorite_Character, Favorite_Planet, Favorite_Vehicle

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_dev.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/flask_db'
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade

@app.route('/api/people', methods=['GET'])
def get_character():
    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))
    return jsonify(characters), 200

@app.route('/api/people/<int:people_id>', methods=['GET'])
def get_characters_by_id(people_id):
    character = Character.query.get(people_id)
    return jsonify(character.serialize()), 200

@app.route('/api/people', methods=['POST'])
def create_characters():
    data = request.get_json()
    character = Character()
    character.name = data['name']
    character.height = data['height']
    character.mass = data['mass']
    character.hair_color = data['hair_color']
    character.skin_color = data['skin_color']
    character.eye_color = data['eye_color']
    character.birth_year = data['birth_year']
    character.gender = data['gender']

    db.session.add(character) # INSERT INTO todos (label, done) VALUES ('My First Task', false);
    db.session.commit() # Finaliza el query

    return jsonify(character.serialize()), 201

@app.route('/api/people/<int:people_id>', methods=['DELETE'])
def delete_characters_by_id(people_id):
    character = Character.query.get(people_id)
    db.session.delete(character)
    db.session.commit()
    return jsonify(character.serialize()), 200

@app.route('/api/planets', methods=['GET'])
def get_planet():
    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(planets), 200

@app.route('/api/planets/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    return jsonify(planet.serialize()), 200

@app.route('/api/planets', methods=['POST'])
def create_planets():
    data = request.get_json()
    planet = Planet()
    planet.name = data['name']
    planet.rotation_period = data['rotation_period']
    planet.orbital_period = data['orbital_period']
    planet.diameter = data['diameter']
    planet.climate = data['climate']
    planet.gravity = data['gravity']
    planet.terrain = data['terrain']
    planet.surface_water = data['surface_water']
    planet.population = data['population']

    db.session.add(planet) # INSERT INTO todos (label, done) VALUES ('My First Task', false);
    db.session.commit() # Finaliza el query

    return jsonify(planet.serialize()), 201

@app.route('/api/planets/<int:planet_id>', methods=['DELETE'])
def delete_planets_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return jsonify(planet.serialize()), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_users_by_id(user_id):
    user = User.query.get(user_id)
    return jsonify(user.serialize()), 200

@app.route('/api/users', methods=['POST'])
def create_users():
    data = request.get_json()
    user = User()
    user.email = data['email']
    user.password = data['password']
    user.name = data['name']
    user.lastname = data['lastname']

    db.session.add(user) # INSERT INTO todos (label, done) VALUES ('My First Task', false);
    db.session.commit() # Finaliza el query

    return jsonify(user.serialize()), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_users_by_id(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize()), 200


if __name__ == '__main__':
    app.run()    