import pytest
from .helpers import Vocabulary, EpithetGenerator
import os
import random


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
