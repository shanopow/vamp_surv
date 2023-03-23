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


    # while our loadouts are not fully finished, fill them out
    def finish_loadout(self):
        while len(self.base_weapon) < 6:
            self.base_weapon.append("Free")
        while len(self.base_item) < 6:
            self.base_item.append("Free")

    def fill_loadout(self, finder, evolve):
        for item in evolve.weapon + evolve.item:
            if item != finder.name:
                if item in evolve.weapon and len(self.base_weapon) < 6:
                    self.base_weapon.append(item)
                elif item in evolve.item and len(self.base_item) < 6:
                    self.base_item.append(item)

    def fill_evolve(self, finder, evolve_list):
        for evolve in evolve_list:
            if (finder.name in evolve.weapon or finder.name in evolve.item) and evolve not in self.base_evolves:
                self.base_evolves.append(evolve)
                self.fill_loadout(finder, evolve)