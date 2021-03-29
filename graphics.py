import pygame
from hexgrid_hex import HexGrid, GraphicHex
import tile_types
from terrain import TerrainFactory

WOODS_IMG = pygame.image.load('bitmaps/Woods.png')

EDGE = (70,70,70)
EDGE_SHADOW = (90, 90, 90)
BACKGROUND = (10,10,10)

DESERT = (235,180,52)

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class HexGraphics:
    def __init__(self, pygame: pygame, hexGrid: HexGrid, terrainFactory: TerrainFactory):
        self.hexGrid = hexGrid
        resolution = (2450,1500)
        self.terrain_factory = terrainFactory
        self.pygame = pygame
        self.screen = pygame.display.set_mode(resolution)
        self.flush()

    def flush(self):
        self.draw_background()
        self.flushTerrain()
        self.draw_edges()

    def draw_background(self):
        self.screen.fill(BACKGROUND)

    def draw_edges(self):
        for hex in self.hexGrid.streamHexes():
            self.pygame.draw.lines(self.screen, EDGE_SHADOW, True, hex.polygon(), 10)

        for hex in self.hexGrid.streamHexes():
            self.pygame.draw.lines(self.screen, BACKGROUND, True, hex.polygon(), 3)

        for hex in self.hexGrid.streamHexes():
            if hex.active:
                self.pygame.draw.lines(self.screen, WHITE, True, hex.polygon(), 5)
                
    # move to hexGrid
    def activateHex(self, clickPoint: tuple):
        hex = self.hexGrid.find(clickPoint)
        if not hex:
            return
        hex.active = not hex.active
        self.flush()

    def drawTerrain(self, hex: GraphicHex):
        #img = hex.terrain.image
        terrain = self.terrain_factory.loaded_terrains.get(hex.terrain_key)
        if not terrain:
            self.pygame.draw.polygon(self.screen, BACKGROUND, hex.polygon())
            return
        img = terrain.image
        rect = img.get_rect()
        rect.center = hex.centerPoint[0], hex.centerPoint[1]
        self.screen.blit(img, rect)
        if hex.woods:
            self.screen.blit(WOODS_IMG, rect)

    def flushTerrain(self):
        for hex in self.hexGrid.streamHexes():
            self.drawTerrain(hex=hex)

