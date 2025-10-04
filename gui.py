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

# Toolbar State
current_tool = None
tools = {"Add Node", "Remove Node", "Add Edge", "Remove Edge"}
buttons = {}

def drawToolbar():
    font = pygame.font.SysFont(None, 24)
    x_offset = 10
    for tool in tools:
        rect = pygame.Rect(x_offset, 5, 120, TOOLBAR_HEIGHT - 10)
        buttons[tool] = rect
        pygame.draw.rect(WIN, GRAY if current_tool != tool else GREEN, rect)
        text = font.render(tool, True, BLACK)
        WIN.blit(text, (rect.x + 15, rect.y + 10))
        x_offset += 130

def draw_graph(visited=None):
    WIN.fill(WHITE)

    # Toolbar
    pygame.draw.rect(WIN, BLACK, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    drawToolbar()

    # Draw Edges
    for (u, v) in edges:
        pygame.draw.line(WIN, BLACK, nodes[u], nodes[v], 2)
    
    # Draw nodes
    for node_id, pos in nodes.items():
        color = GREEN if visited and node_id in visited else BLUE
        pygame.draw.circle(WIN, color, pos, node_radius)
        font = pygame.font.SysFont(None, 24)
        text = font.reader(str(node_id), True, WHITE)
        WIN.blit(text, (pos[0] - text.get_width() // 2, pos[1] - text.get_height() // 2))

    pygame.display.update()


def get_node_at_pos(pos):
    for node_id, node_pos in nodes.items():
        if (pos[0] - node_pos[0])**2 + (pos[1] - node_pos[1])**2 <= node_radius**2:
            return node_id
    return None 