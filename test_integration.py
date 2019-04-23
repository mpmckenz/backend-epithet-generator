import json
from flask import Flask
from flask_testing import TestCase
from backend_epithet_generator.app import app

app.config['TESTING'] = True


def test_random_epithat():
    response = app.test_client().get('/')
    data = response.data.decode()
    assert type(data) == str
    assert response.json, dict(success=True)


def test_vocabulary():
    response = app.test_client().get('/vocabulary')
    data = response.data.decode()
    assert response.json, dict(success=True)
    assert type(data) == str


def test_multiple_epithets():
    response = app.test_client().get('/multiple_epithets')
    data = response.data.decode()
    assert isinstance(data, str)
    assert 1 <= len(data.split(',')) <= 20
