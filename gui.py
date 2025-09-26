import pygame
import sys
import algorithms

pygame.init()
WIDTH, HEIGHT = 900, 600
TOOLBAR_HEIGHT = 50
WIN = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Graph Editor")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Graph data
nodes = {}
edges = []
node_radius = 25
dragging_node = None
node_id_corner = 0