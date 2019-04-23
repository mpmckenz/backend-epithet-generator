import os
import pytest
from .helpers import Vocabulary, EpithetGenerator
from flask import Flask
import requests


app = Flask(__name__)


def test_http():
    """http status check WHEN app is running"""
    response_random = requests.get('http://127.0.0.1:5000/')
    response_vocab = requests.get('http://127.0.0.1:5000/vocabulary')
    response_multiple_epi = requests.get(
        'http://127.0.0.1:5000/multiple_epithets')
    assert response_random.status_code == 200
    assert response_vocab.status_code == 200
    assert response_multiple_epi.status_code == 200


def test_fail_vocab():
    with pytest.raises(AssertionError):
        assert Vocabulary().read_json() == ''


def test_vocab():
    assert os.path.exists("resources/data.json")


def test_fail_epithet():
    with pytest.raises(AssertionError):
        assert len(EpithetGenerator().epithet_generator().split(' ')) != 4


def test_epithet():
    assert "ill-breeding" in EpithetGenerator().epithet_vocab()
