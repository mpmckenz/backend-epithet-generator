import os
import pytest
from .helpers import Vocabulary, EpithetGenerator
import requests
# import app from app


def test_http():
    """http status check WHEN app is running"""
    response_random = requests.get('http://127.0.0.1:5000/')
    response_vocab = requests.get('http://127.0.0.1:5000/vocabulary')
    response_multiple_epi = requests.get(
        'http://127.0.0.1:5000/epithets/3')
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


def test_epi_qty():
    assert len(EpithetGenerator().generate_epithet_quantity(3)
               ) == 3


def test_fail_api_qty():
    assert isinstance(EpithetGenerator().generate_epithet_quantity(10), list)
