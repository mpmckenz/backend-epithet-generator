from flask import Flask
# from dotenv import load_dotenv
from .helpers import EpithetGenerator


app = Flask(__name__)


@app.route('/')
def random_epithat():
    return EpithetGenerator().epithet_generator()


@app.route('/vocabulary')
def vocabulary():
    return EpithetGenerator().epithet_vocab()
