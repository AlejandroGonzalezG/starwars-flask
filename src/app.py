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


@app.route('/') #Página principal del app.py
def main():
    return jsonify({ "msg": "WELCOME TO SWAPI REST FLASK" }), 200

@app.route('/api/people', methods=['GET']) #Entrega en listado de los characters creados en la base de datos(por ahora esta vacía) o usando el método GET
def get_character():
    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))
    return jsonify(characters), 200

@app.route('/api/people/<int:people_id>', methods=['GET']) #Entrega toda la información del usuario consultado a través del id
def get_characters_by_id(people_id):
    character = Character.query.get(people_id)
    return jsonify(character.serialize()), 200

@app.route('/api/people', methods=['POST']) #Obtiene los datos del Character a través de POST y crea un Character nuevo.
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

    db.session.add(character)
    db.session.commit()

    return jsonify(character.serialize()), 201

@app.route('/api/people/<int:people_id>', methods=['DELETE']) #Según el id enviado, elimina un character de los creados a través de POST
def delete_characters_by_id(people_id):
    character = Character.query.get(people_id)
    db.session.delete(character)
    db.session.commit()
    return jsonify(character.serialize()), 200

@app.route('/api/planets', methods=['GET']) #Entrega el listado de los planetas creados a través de 
def get_planet():
    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(planets), 200

@app.route('/api/planets/<int:planet_id>', methods=['GET']) #Entrega según el id enviado el Planeta correspondiente de los creados
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    return jsonify(planet.serialize()), 200

@app.route('/api/planets', methods=['POST']) #Obtiene los datos del Planet a través de POST y crea un Planet nuevo.
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

    db.session.add(planet) 
    db.session.commit() 

    return jsonify(planet.serialize()), 201

@app.route('/api/planets/<int:planet_id>', methods=['DELETE']) #Según el id enviado, elimina un planet de los creados a través de POST
def delete_planets_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return jsonify(planet.serialize()), 200

@app.route('/api/users', methods=['GET']) #Entrega en listado de los usuarios creados en la base de datos(por ahora esta vacía) o usando el método GET
def get_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200

@app.route('/api/users/<int:user_id>', methods=['GET']) #Entrega todos los atributos del usuario consultado a través del id
def get_users_by_id(user_id):
    user = User.query.get(user_id)
    return jsonify(user.serialize()), 200

@app.route('/api/users', methods=['POST']) #Crea usuario nuevos según lo enviado a través de POST
def create_users():
    data = request.get_json()
    user = User()
    user.email = data['email']
    user.password = data['password']
    user.name = data['name']
    user.lastname = data['lastname']
    


    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE']) #Elimina un usuario de la base de datos o los enviados por el método POST
def delete_users_by_id(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize()), 200

@app.route('/api/users/favorites/<int:user_id>', methods=['GET']) #A través del usuario consultado con el id entrega el nombre y la lista de favoritos que haya agregado el id del Usuario
def get_users_by_id_and_favorites(user_id):
    user = User.query.get(user_id)
    return jsonify({ "Name": user.name, "Favorites Planets": list(map(lambda planet:planet.name, user.planets_favorites)), "Favorites Characters": user.characters_favorites }), 200

@app.route('/api/favorite/planet/<int:id>', methods=['PUT']) #Agrega o quita de los favoritos Planets al usuario según el id del usuario entregando los favoritos a través del método PUT como una lista [] 
def favorite_planets_update(id):

    username = request.json.get('name')
    planets_favorite = request.json.get('planets_favorite')

    user = User.query.get(id)
    #user.username = username
    #user.password = generate_password_hash(password)

    if planets_favorite:
        for planet in user.planets_favorites:
            if not planet.id in planets_favorite:
                user.planets_favorites.remove(planet)

        for planet in planets_favorite:
            new_planet = Planet.query.get(planet)
            if not new_planet in user.planets_favorites:
                user.planets_favorites.append(new_planet)

    db.session.commit()


    return jsonify(user.serialize()), 200

@app.route('/api/favorite/character/<int:id>', methods=['PUT']) #Agrega o quita de los favoritos Characters al usuario según el id del usuario entregando los favoritos a través del método PUT como una lista [] 
def favorite_characters_update(id):

    username = request.json.get('name')
    characters_favorite = request.json.get('characters_favorite')

    user = User.query.get(id)
    #user.username = username
    #user.password = generate_password_hash(password)

    if characters_favorite:
        for character in user.characters_favorites:
            if not character.id in characters_favorite:
                user.characters_favorites.remove(character)

        for character in characters_favorite:
            new_character = Character.query.get(character)
            if not new_character in user.characters_favorites:
                user.characters_favorites.append(new_character)

    db.session.commit()


    return jsonify(user.serialize()), 200


if __name__ == '__main__':
    app.run()    

