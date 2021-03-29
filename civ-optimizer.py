import pygame, sys
from pygame.locals import *
from hexgrid_hex import GraphicHex, HexGrid
from graphics import HexGraphics
import tile_types
import terrain
import pickle
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
#DISPLAYSURF = pygame.display.set_mode((2000,2000))
#DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Civ 6 District Optimizer")



hexGrid = HexGrid((15,12))
#edges_drawed = []
factory = terrain.TerrainFactory()
graphics = HexGraphics(pygame=pygame, hexGrid=hexGrid, terrainFactory=factory)





#draw_edges(pygame, DISPLAYSURF, hexGrid)

#for hex in hexGrid.streamHexes():
#    pygame.draw.aalines(DISPLAYSURF, hex.color, True, hex.polygon())
    #for edge in hex.edges():
    #    if not edge in edges_drawed:
    #        pygame.draw.line(DISPLAYSURF, hex.color, edge[0], edge[1])
    #        edges_drawed.append(edge)

# Creating Lines and Shapes
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
#pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
#pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
#pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
#pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
#pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
 
# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            graphics.activateHex(pos)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hexGrid.setTerrainForActives(terrain=factory.iterate_terrain(-1,0))

            if event.key == pygame.K_RIGHT:
                hexGrid.setTerrainForActives(terrain=factory.iterate_terrain(1,0))

            if event.key == pygame.K_UP:
                hexGrid.setTerrainForActives(terrain=factory.iterate_terrain(0,1))

            if event.key == pygame.K_DOWN:
                hexGrid.setTerrainForActives(terrain=factory.iterate_terrain(0,-1))


            if event.key == pygame.K_d:
                hexGrid.setTerrainForActives(terrain_key='desert')
            if event.key == pygame.K_p:
                hexGrid.setTerrainForActives(terrain_key='plains')
            if event.key == pygame.K_g:
                hexGrid.setTerrainForActives(terrain_key='grassland')
            if event.key == pygame.K_o:
                hexGrid.setTerrainForActives(terrain_key='oasis')
            if event.key == pygame.K_w:
                hexGrid.setWoodsForActives()
            
            if event.key == pygame.K_s:
                with open('save_map.pkl', 'wb') as f:
                    pickle.dump(hexGrid, f, pickle.HIGHEST_PROTOCOL)

            if event.key == pygame.K_l:
                with open('save_map.pkl', 'rb') as f:
                    hexGrid = pickle.load(f)
                    graphics.hexGrid = hexGrid

            if event.key == pygame.K_q:
                hexGrid.deactivateHexes()
            graphics.flush()
            #hexGrid.click(pos)
            #for hex in hexGrid.streamHexes():
            #    for edge in hex.edges():
            #        pygame.draw.line(DISPLAYSURF, hex.color, edge[0], edge[1])
            #    pygame.draw.polygon(DISPLAYSURF, hex.color, hex.polygon())

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)
