class Weapon(object):
    def __init__(self, holder):
        self.name = holder["name"]
        self.locations = holder["locations"]

class Item(object):
    def __init__(self, holder):
        self.name = holder["name"]
        self.locations = holder["locations"]

class Evolve(object):
    def __init__(self, holder):
        self.name = holder["name"]
        self.weapon = holder["weapon"]
        self.item = holder["item"]

class Union(object):
    def __init__(self, holder):
        self.name = holder["name"]
        self.weapon = holder["weapon"]
        self.item = holder["item"]

class Loadout(object):
    def __init__(self):
        self.base_weapon = []
        self.base_item = []
        self.base_evolves = []
        # weapons / items already on the map to take
        self.extra_weapon = []
        self.extra_item = []
