import json
import random


class Vocabulary:
    """
    Handle loading in a JSON file with proper unfinished swears in it!
    """

    def read_json(path, mode='r'):
        """Loads a json file"""
        path = "resources/data.json"
        with open(path, mode=mode) as handle:
            return json.load(handle)


class EpithetGenerator:
    """
    1. select one random word from each column of the list.
    2. generate a quantity of epithets from a vocabulary file loaded from a path.
    """

    def epithet_read(self):
        """Reads json"""
        path = "resources/data.json"
        data = Vocabulary.read_json(path)
        return data

    def epithet_generator(self):
        """Returns epithet phrase"""
        ep_phrase = 'Thou {} {} {}'.format(random.choice(data['Column 1']), random.choice(
            data['Column 2']), random.choice(data['Column 3']))
        return ep_phrase

    def epithet_vocab(self):
        """Returns epithet vocabulary"""
        result = str(data['Column 1'] + data['Column 2'] + data['Column 3'])
        return result

    def generate_epithet_quantity(self, qty):
        epi_container = []
        for number in range(int(qty)):
            epi_container.append(EpithetGenerator().epithet_generator())
        return epi_container


data = EpithetGenerator().epithet_read()
