from flask import Flask, jsonify
from .helpers import EpithetGenerator
import random

app = Flask(__name__)


@app.route('/')
def random_epithat():
    epithets = {"epithets": [EpithetGenerator().epithet_generator()]}
    return jsonify(epithets['epithets'])


@app.route('/vocabulary')
def vocabulary():
    vocabulary = {"vocabulary": [EpithetGenerator().epithet_vocab()]}
    return jsonify(vocabulary['vocabulary'])


@app.route('/multiple_epithets')
def multiple_epithets():
    multiplier = random.randint(1, 21)
    epi_container = []
    for number in range(multiplier):
        epi_container.append(EpithetGenerator().epithet_generator())
    return str(epi_container)
