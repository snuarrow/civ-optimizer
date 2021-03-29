
        
import pygame

GRASSLAND = pygame.image.load('bitmaps/Grassland.png')
DESERT = pygame.image.load('bitmaps/Desert.png')
PLAINS = pygame.image.load('bitmaps/Plains.png')
OASIS = pygame.image.load('bitmaps/Oasis.png')
DESERT_FLOODPLAINS = pygame.image.load('bitmaps/Desert_Floodplains.png')



class Tile:

    def __init__(self, hills: bool = False, food: int = 0, production: int = 0, gold: int = 0, science: int = 0, culture: int = 0, image: pygame.Surface = None):
        self.hills = hills
        self.food = food
        self.production = production
        self.gold = gold
        self.science = science
        self.culture = culture
        self.image = image

        if hills:
            production += 1

class Plains(Tile):
    def __init__(self):
        print(self.__class__.__name__)
        super().__init__(food = 1, production = 1, image=PLAINS)

class Desert(Tile):
    def __init__(self):
        super().__init__(image=DESERT)

class GrassLand(Tile):
    def __init__(self):
        super().__init__(food = 2, image=GRASSLAND)

class Oasis(Tile):
    def __init__(self):
        super().__init__(food = 3, gold = 1, image=OASIS)

class DesertFloodplains(Tile):
    def __init__(self):
        super().__init__(food = 3, gold = 1, image=DESERT_FLOODPLAINS)
