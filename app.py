from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def random_epithat():
    return jsonify({"epithets": []})

@app.route('/vocabulary')
def vocabulary():
    return jsonify({"vocabulary": {}})