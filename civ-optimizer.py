import pygame, sys
from pygame.locals import *
from hexgrid_hex import GraphicHex, HexGrid
from graphics import HexGraphics
import tile_types
import terrain
import pickle
from human_interface import HumanInterface

pygame.init()
FPS = 30
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Civ 6 District Optimizer")
hexGrid = HexGrid((15,12))
factory = terrain.TerrainFactory()
graphics = HexGraphics(pygame=pygame, hexGrid=hexGrid, terrainFactory=factory)
interface = HumanInterface(hexGrid, factory, graphics)

while True:
    pygame.display.update()
    interface.handle_event(pygame.event.get())
    FramePerSec.tick(FPS)
