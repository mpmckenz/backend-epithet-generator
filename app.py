from flask import Flask
from .helpers import EpithetGenerator


app = Flask(__name__)


@app.route('/')
def random_epithat():
    return EpithetGenerator().epithet_generator()


@app.route('/vocabulary')
def vocabulary():
    return EpithetGenerator().epithet_vocab()


@app.route('/epithets/<qty>')
def multiple_epithets(qty):
    return str(EpithetGenerator().generate_epithet_quantity(qty))
