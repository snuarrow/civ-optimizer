import math
import random
from tile_types import *
from terrain import *

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
PINK  = (255, 0, 255)


class GraphicHex:

    neighbours = []
    active = False

    def __init__(self, centerPoint: tuple, radius: int, identifier: int):
        self.id = identifier
        x, y = centerPoint
        self.radius = radius
        self.centerPoint = centerPoint
        self.north = x, y - radius
        self.south = x, y + radius
        self.north_west = x - (0.866 * radius), y - (0.5 * radius)
        self.south_west = x - (0.866 * radius), y + (0.5 * radius)
        self.north_east = x + (0.866 * radius), y - (0.5 * radius)
        self.south_east = x + (0.866 * radius), y + (0.5 * radius)
        #self.terrain = Terrain()
        self.terrain_key = None
        self.woods = False

    def polygon(self):
        return (self.north,self.north_east,self.south_east,self.south,self.south_west,self.north_west)


    def edges(self):
        return [
            (self.north, self.north_east),
            (self.north_east, self.south_east),
            (self.south_east, self.south),
            (self.south, self.south_west),
            (self.south_west, self.north_west),
            (self.north_west, self.north),
        ]

    def hit(self, centerPoint: tuple):
        xDist = abs(centerPoint[0] - self.centerPoint[0])
        yDist = abs(centerPoint[1] - self.centerPoint[1])
        dist = math.sqrt(xDist*xDist + yDist*yDist)
        return dist < (self.radius * 0.866)

    def setTerrain(terrain: Tile):
        self.terrain = terrain

class HexGrid:
    def __init__(self, gridResolution: tuple):
        self.hexes = []
        radius = 100
        identifier = 0
        x, y = -0.1*radius, 0 
        even = False
        for _ in range(gridResolution[1]):
            for _ in range(gridResolution[0]):
                hex = GraphicHex((x,y), radius, identifier)
                identifier += 1
                self.hexes.append(hex)
                x += 2 * 0.866 * radius
            if even:
                x = -0.1*radius
                even = False
            else:
                x = -0.1*radius + radius*0.866
                even = True
            y += 1.5*radius

        self._buildRelations()

    def _buildRelations(self):
        for currentHex in self.hexes:
            x, y = currentHex.centerPoint
            radius = currentHex.radius
            neighbours = []
            for offset in [(1.5,0),(1,1.5),(-1, 1.5),(-1.5,0),(-1, -1.5),(1, -1.5)]:
                hex = self.find((offset[0] * radius + x, offset[1] * radius + y))
                if hex:
                    neighbours.append(hex)
            
            currentHex.neighbours = neighbours
            
            
    def streamHexes(self):
        for hex in self.hexes:
            yield hex

    def click(self, point: tuple):
        hex = self.find(point)
        if not hex:
            return
        hex.color = RED
        for neighbour in hex.neighbours:
            neighbour.color = PINK

    def find(self, point: tuple):
        for hex in self.hexes:
            if (hex.hit(point)):
                return hex

    def deactivateHexes(self):
        for hex in self.hexes:
            hex.active = False

    def setTerrainForActives(self, terrain_key: str):
        for hex in self.hexes:
            if hex.active:
                hex.terrain_key = terrain_key
                #hex.terrain = factory.make_terrain(key)

    def setWoodsForActives(self):
        for hex in self.hexes:
            if hex.active:
                hex.woods = not hex.woods
