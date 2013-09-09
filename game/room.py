import json
import os


def get_room(id):
    ret = None
    with open(os.path.join(
             os.path.dirname(__file__), 'rooms/' + str(id) + '.json'),
          'r') as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room(**d)
    return ret


class Room():
    def __init__(self, id=0, name='A room', description='An empty room',
        neighbors={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self._neighbor('n')

    def south(self):
        return self._neighbor('s')

    def east(self):
        return self._neighbor('e')

    def west(self):
        return self._neighbor('w')

    def climb(self):
        return self._neighbor('climb')

    def enter(self):
        return self._neighbor('enter')

    def blacksmith(self):
        return self._neighbor('blacksmith')

    def forge(self):
        return self._neighbor('forge')

    def leave(self):
        return self._neighbor('leave')