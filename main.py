import pygame
from config import *
from player import Player
from drawing import Drawing

pygame.init()
pygame.display.set_caption(game.name)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
mapscreen = pygame.Surface((WIDTH // minimap.scale, HEIGHT // minimap.scale))
clock = pygame.time.Clock()
player = Player()
draw = Drawing(screen, mapscreen)
hud_id = 0

while True:

    if hud_id == 2:
        player.movement()

    draw.bg(player.angle)
    draw.tiles(player.pos, player.angle)
    hud_id = draw.hud(clock, player.pos, player.angle)

    pygame.display.flip()
    clock.tick(game.fps)