from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

import os

app = Flask(__name__)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

flask_app = os.getenv('FLASK_APP')
flask_env = os.getenv('FLASK_ENV')

@app.route('/')
def random_epithat():
    return jsonify({"epithets": []})

@app.route('/vocabulary')
def vocabulary():
    return jsonify({"vocabulary": {}})