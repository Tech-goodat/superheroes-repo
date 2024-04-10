from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    hero_powers=db.relationship('HeroPower', back_populates='hero')

    # add serialization rules

    def __repr__(self):
        return f'<Hero {self.id}>'


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    hero_power=db.relationship('HeroPower', back_populates='power')


    # add serialization rules

    # add validation

    def __repr__(self):
        return f'<Power {self.id}>'


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)

    hero_id=db.Column(db.Integer, db.ForeignKey('heroes.id'))
    hero=db.relationship('Hero', back_populates=('hero_powers'))
    
    power_id=db.Column(db.Integer, db.ForeignKey('powers.id'))
    power=db.relationship('Power', back_populates='hero_powers')

    # add validation

    def __repr__(self):
        return f'<HeroPower {self.id}>'
