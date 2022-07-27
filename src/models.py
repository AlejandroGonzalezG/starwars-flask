import os
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
db = SQLAlchemy()

class User(db.Model):
    __tablename__='Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80))
    lastname = db.Column(db.String(80))

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "lastname": self.lastname
        }

class Character(db.Model):
    __tablename__='Characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    height = db.Column(db.Integer)		
    mass = db.Column(db.Integer)		
    hair_color = db.Column(db.String(80))	
    skin_color = db.Column(db.String(80))		
    eye_color = db.Column(db.String(80))		
    birth_year = db.Column(db.String(80))		
    gender = db.Column(db.String(80))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    __tablename__='Planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))		
    rotation_period = db.Column(db.Integer)		
    orbital_period = db.Column(db.Integer)	
    diameter = db.Column(db.Integer)		
    climate = db.Column(db.String(80))		
    gravity = db.Column(db.String(80))
    terrain = db.Column(db.String(80))
    surface_water = db.Column(db.Integer)		
    population = db.Column(db.String(80))		

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
        }

class Film(db.Model):
    __tablename__='Films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))		
    episode_id = db.Column(db.Integer)		
    opening_crawl = db.Column(db.Text(500))		
    director = db.Column(db.String(80))		
    producer = db.Column(db.String(80))		
    release_date = db.Column(db.Date)		

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "episode_id": self.episode_id,
            "opening_crawl": self.opening_crawl,
            "director": self.director,
            "producer": self.producer,
            "release_date": self.release_date,
        }

class Specie(db.Model):
    __tablename__='Species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))		
    classification = db.Column(db.String(80))		
    average_height = db.Column(db.Integer)		
    skin_colors = db.Column(db.String(80))		
    hair_colors = db.Column(db.String(80))		
    eye_colors = db.Column(db.String(80))		
    average_lifespan = db.Column(db.Integer)		
    language = db.Column(db.String(80))		

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "average_height": self.average_height,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "average_lifespan": self.average_lifespan,
            "language": self.language,
        }

class Vehicle(db.Model):
    __tablename__='Vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))		
    model = db.Column(db.String(80))		
    manufacturer = db.Column(db.String(80))		
    cost_in_credits = db.Column(db.Integer)	
    lenght = db.Column(db.Float)		
    max_atmosphering_speed = db.Column(db.Integer)	
    crew = db.Column(db.Integer)		
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(80))		
    vehicle_class = db.Column(db.String(80))		

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "lenght": self.lenght,
            "max_atmosphering": self.max_atmosphering,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "vehicle_class": self.vehicle_class,
        }

class Starship(db.Model):
    __tablename__='Starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))		
    model = db.Column(db.String(80))		
    manufacturer = db.Column(db.String(80))		
    cost_in_credits = db.Column(db.Integer)		
    lenght = db.Column(db.Integer)		
    max_atmosphering_speed = db.Column(db.Integer)		
    crew = db.Column(db.String(80))		
    passengers = db.Column(db.Integer)		
    cargo_capacity = db.Column(db.Integer)		
    consumables = db.Column(db.String(80))		
    hyperdrive_rating = db.Column(db.String(80))		
    MGLT = db.Column(db.Integer)		
    starship_class = db.Column(db.String(80))		

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "lenght": self.lenght,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "starship_class": self.starship_class,
        }

class Favorite_Character(db.Model):
    __tablename__= 'Favorites Characters'
    users_id = db.Column(db.Integer, db.ForeignKey("Users.id"), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("Characters.id"), primary_key=True)

    def serialize(self):
        return {
            "users_id": self.users_id,
            "people_id": self.people_id,
        }

class Favorite_Vehicle(db.Model):
    __tablename__= 'Favorites Vehicles'
    users_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("Vehicles.id"), primary_key=True)

    def serialize(self):
        return {
            "users_id": self.users_id,
            "vehicle_id": self.vehicle_id,
        }

class Favorite_Planet(db.Model):
    __tablename__= 'Favorites Planets'
    users_id = db.Column(db.Integer, db.ForeignKey("Users.id"), primary_key=True)
    planets_id = db.Column(db.Integer, db.ForeignKey("Planets.id"), primary_key=True)

    def serialize(self):
        return {
            "users_id": self.users_id,
            "planets_id": self.planets_id,
        }

