from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])


@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict())
    else:
        return jsonify({'error': 'Hero not found'}), 404


@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])


@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def power(id):
    if request.method == 'GET':
        power = Power.query.get(id)
        if power:
            return jsonify(power.to_dict())
        else:
            return jsonify({'error': 'Power not found'}), 404
    elif request.method == 'PATCH':
        power = Power.query.get(id)
        if not power:
            return jsonify({'error': 'Power not found'}), 404

        data = request.json
        description = data.get('description')

        if description:
            power.description = description
            db.session.commit()
            return jsonify(power.to_dict())
        else:
            return jsonify({'error': 'Invalid request'}), 400


@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')

    if not (strength and power_id and hero_id):
        return jsonify({'error': 'Invalid request'}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    if not (hero and power):
        return jsonify({'error': 'Invalid hero or power'}), 400

    hero_power = HeroPower(strength=strength, hero=hero, power=power)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify(hero_power.to_dict()), 201


@app.route('/')
def index():
    return '<h1>Code challenge</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
