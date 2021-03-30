from hexgrid_hex import HexGrid
from terrain import TerrainFactory
from graphics import HexGraphics
import pygame
import pickle
import sys

class HumanInterface:
    def __init__(self, hex_grid: HexGrid, terrain_factory: TerrainFactory, graphics: HexGraphics):
        self.hex_grid = hex_grid
        self.terrain_factory = terrain_factory
        self.graphics = graphics

    def handle_event(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.graphics.activateHex(pos)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.hex_grid.setTerrainForActives(terrain_key=self.terrain_factory.iterate_terrain(-1,0))

                if event.key == pygame.K_RIGHT:
                    self.hex_grid.setTerrainForActives(terrain_key=self.terrain_factory.iterate_terrain(1,0))

                if event.key == pygame.K_UP:
                    self.hex_grid.setTerrainForActives(terrain_key=self.terrain_factory.iterate_terrain(0,1))

                if event.key == pygame.K_DOWN:
                    self.hex_grid.setTerrainForActives(terrain_key=self.terrain_factory.iterate_terrain(0,-1))


                if event.key == pygame.K_d:
                    self.hex_grid.setTerrainForActives(terrain_key='desert')
                if event.key == pygame.K_p:
                    self.hex_grid.setTerrainForActives(terrain_key='plains')
                if event.key == pygame.K_g:
                    self.hex_grid.setTerrainForActives(terrain_key='grassland')
                if event.key == pygame.K_o:
                    self.hex_grid.setTerrainForActives(terrain_key='oasis')
                if event.key == pygame.K_w:
                    self.hex_grid.setWoodsForActives()

                if event.key == pygame.K_s:
                    with open('save_map.pkl', 'wb') as f:
                        pickle.dump(self.hex_grid, f, pickle.HIGHEST_PROTOCOL)

                if event.key == pygame.K_l:
                    with open('save_map.pkl', 'rb') as f:
                        self.hex_grid = pickle.load(f)
                        self.graphics.hexGrid = self.hex_grid

                if event.key == pygame.K_q:
                    self.hex_grid.deactivateHexes()
                self.graphics.flush()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

