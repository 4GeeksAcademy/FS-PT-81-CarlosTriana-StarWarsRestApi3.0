from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
            # do not serialize the password, its a security breach
        }
    



class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people = db.Column(db.String(30), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    planet = db.Column(db.String(30), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'people': self.people,
            'gender': self.gender,
            'planet': self.planet
        }
    


class Peoples(db.Model):
    __tablename__='peoples'
    id = db.Column(db.Integer, primary_key=True)
    people = db.Column(db.String(80), unique=True, nullable=False)
    gender = db.Column(db.String(20), nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)
    eye_color = db.Column(db.String(20), nullable=True)
    hair_color = db.Column(db.String(20), nullable=True)
    height = db.Column(db.Float, nullable=True)
    mass = db.Column(db.Float, nullable=True)
    skin_color = db.Column(db.String(20), nullable=True)
    #planets = db.relationship('Planets', backref='peoples')
    #favorites = db.relationship('Favorites', backref='peoples')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __repr__(self):
         return '<Peoples %r>' % self.people

    def serialize(self):
        return {
            "id" : self.id,
            "people" : self.people,
            "gender" : self.gender,
            "birth_year": self.birth_year,
            "eye_color" : self.eye_color,
            "hair_color" : self.hair_color,
            "height": self.height,
            "mass" : self.mass,
            "skin_color" : self.skin_color
            # do not serialize the password, its a security breach
        }



class Planets(db.Model):
    __tablename__='planets'
    id = db.Column(db.Integer, primary_key=True)
    planet = db.Column(db.String(80), unique=True, nullable=False)
    rotation_period = db.Column(db.Float, nullable=True)
    orbital_period = db.Column(db.Float, nullable=True)
    gravity = db.Column(db.String(20), nullable=True)
    population = db.Column(db.Integer, nullable=True)
    climate = db.Column(db.String(20), nullable=True)
    terrain = db.Column(db.String(20), nullable=True)
    surface_water = db.Column(db.Float, nullable=True)
    #people_id = db.Column(db.Integer, db.ForeignKey('peoples.id'), nullable=True)
    #favorites = db.relationship('Favorites', backref='planets')

    def __repr__(self):
         return '<Planets %r>' % self.planet

    def serialize(self):
        return {
            "id" : self.id,
            "planet" : self.planet,
            "rotation_period" : self.rotation_period,
            "orbital_period" : self.orbital_period,
            "gravity" : self.gravity,
            "population" : self.population,
            "climate": self.climate,
            "terrain" : self.terrain,
            "surface_water" : self.surface_water
            # do not serialize the password, its a security breach
        }
    
