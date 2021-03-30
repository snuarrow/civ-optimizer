import pygame
from os import listdir

class Terrain:

    def __init__(self, food: int = 0, production: int = 0, gold: int = 0, science: int = 0, culture: int = 0, image: pygame.Surface = None):
        self.food = food
        self.production = production
        self.gold = gold
        self.science = science
        self.culture = culture
        self.image = image


class TerrainFactory():
    loaded_terrains = {}

    category_iterator = 0
    rule_iterator = 0

    rules = [
        {
            'desert': {},
            'desert_floodplains': {
                'food': 3,
                'gold': 1,
            },
            'oasis': {
                'food': 3,
                'gold': 1,
            },
            'desert_mountains': {}
        },
        {
            'plains': {
                'food': 1,
                'production': 1
            },
            'plains_hills': {
                'food': 1,
                'production': 2
            },
            'plains_mountains': {}
        },
        {
            'grassland': {
                'food': 2
            },
            'grassland_floodplains': {
                'food': 2
            },
            'marsh': {
                'food': 3
            },
            'grassland_mountains': {}
        },
        {
            'tundra': {
                'food': 1
            },
            'tundra_hills': {
                'food': 1,
                'production': 1
            },
            'tundra_mountains': {}
        },
        {
            'snow': {},
            'snow_hills': {
                'production': 1
            },
            'snow_mountains': {}
        }
    ]

    def __init__(self):
        for file in listdir('bitmaps'):
            if file.endswith('.png') and file != 'Woods.png':
                key = file[:-4].lower()
                self.loaded_terrains[key] = Terrain(**self._find_rule(key), image=pygame.image.load(f'bitmaps/{file}'))

    def _find_rule(self, keyword: str):
        for category in self.rules:
            for rule in category:
                if keyword.lower() == rule.lower():
                    return category[rule]

    def iterate_terrain(self, category_modifier: int, rule_modifier: int):
        if category_modifier != 0:
            self.category_iterator += category_modifier
            if self.category_iterator >= len(self.rules):
                self.category_iterator = 0
            if self.category_iterator < 0:
                self.category_iterator = len(self.rules) - 1
            self.rule_iterator = 0
        
        if rule_modifier != 0:
            self.rule_iterator += rule_modifier
            if self.rule_iterator < 0:
                self.rule_iterator = len(self.rules[self.category_iterator]) - 1
            if self.rule_iterator >= len(self.rules[self.category_iterator]):
                self.rule_iterator = 0
        key = list(self.rules[self.category_iterator])[self.rule_iterator]
        return key
