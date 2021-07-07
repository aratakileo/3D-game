import math

#screen
WIDTH = 1200
HEIGHT = 800

hWIDTH = WIDTH//2
hHEIGHT = HEIGHT//2
double_pi = 2 * math.pi
class game:
    name = '3D game'
    fps = 60

class tile:
    size = 100

class ray:
    fov = math.pi / 3
    hfov = fov / 2
    count = 300
    maxdepth = HEIGHT
    dist = count / (2 * math.tan(hfov))
    coef = 3 * dist * tile.size
    scale = WIDTH // count

class delta():
    angle = ray.fov / ray.count

#player
class pdata:
    pos = (hWIDTH, hHEIGHT)
    angle = 0
    speed = 5

#colors
class color:
    white = (255,255,255)
    black = (0,0,0)
    red = (220,0,0)
    green = (0, 80, 0)
    blue = (0, 0, 255)
    darkgray = (40,40,40)
    purple = (120, 0, 120)
    lightblue = (0, 186, 255)
    yellow = (220, 220, 0)
    lightyellow = (244, 164, 96)

class minimap:
    scale = 5
    tile = tile.size // scale
    pos = (0, HEIGHT - HEIGHT // scale)

txtmap = [
    '@@@@@@@@@@@@',
    '@          @',
    '@  @##@    @',
    '@  @     @ @',
    '@  @ @     @',
    '@  @   #   @',
    '@          @',
    '@@@####@@@@@'
]

class textures:
    mainpath = 'textures/'
    tiles = ['tile1.png', 'tile2.png']
    bgs = ['sky.png']

    width = 1200
    height = 1200
    scale = width // tile.size

class sep:
    width = 17
    height = 17

    size = 6
    outline = 2