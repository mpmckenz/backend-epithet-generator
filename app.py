from flask import Flask, jsonify
from .helpers import EpithetGenerator

app = Flask(__name__)


@app.route('/')
def random_epithat():
    epithets = {"epithets": [EpithetGenerator().epithet_generator()]}
    return jsonify(epithets['epithets'])


@app.route('/vocabulary')
def vocabulary():
    vocabulary = {"vocabulary": [EpithetGenerator().epithet_vocab()]}
    return jsonify(vocabulary['vocabulary'])


@app.route('/epithets/<qty>')
def multiple_epithets(qty):
    return str(EpithetGenerator().generate_epithet_quantity(qty))
