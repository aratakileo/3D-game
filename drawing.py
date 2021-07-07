import pygame
import math
from config import *

#map
wmap = {}
mmap = set()
for j, row in enumerate(txtmap):
    for i, char in enumerate(row):
        if char != ' ':
            mmap.add((i * minimap.tile, j * minimap.tile))
            wmap[(i * tile.size, j * tile.size)] = char

def mapping(a, b):
    return (a // tile.size) * tile.size, (b // tile.size) * tile.size

class Drawing:
    def __init__(self, screen, mapscreen):
        self.screen = screen
        self.mapscreen = mapscreen
        self.font = pygame.font.SysFont('Arial', 20, bold=True)
        self.title = pygame.font.SysFont('Arial', 150, bold=True)
        self.defolt = pygame.font.SysFont('Roboto', 50, bold=True)
        self.textures = {
            '@': pygame.image.load(textures.mainpath + textures.tiles[0]).convert(),
            '#': pygame.image.load(textures.mainpath + textures.tiles[1]).convert(),
            'sky': pygame.image.load(textures.mainpath + textures.bgs[0]).convert()
        }
        self.hudkeypos = 0
        self.buttons = ['Start', 'Exit', 'Yes', 'No']
        self.hud_show = False
        self.hud_id = 0

    def bg(self, angle):
        sky_off = -5 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures['sky'], (sky_off, 0))
        self.screen.blit(self.textures['sky'], (sky_off - WIDTH, 0))
        self.screen.blit(self.textures['sky'], (sky_off + WIDTH, 0))
        # pygame.draw.rect(self.screen, color.lightblue, (0, 0, WIDTH, hHEIGHT))
        pygame.draw.rect(self.screen, color.darkgray, (0, hHEIGHT, WIDTH, hHEIGHT))

    def hud(self, clock, p_pos, p_angle):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.hud_id == 2 or self.hud_id == 0:
                    self.hudkeypos = 1
                    self.hud_id = 1
                    self.hud_show = False
            elif event.type == pygame.KEYDOWN:
                if self.hud_id == 2 or self.hud_id == 0:
                    if event.key == pygame.K_ESCAPE:
                        self.hudkeypos = 1
                        self.hud_id = 1
                        self.hud_show = False
                if self.hud_id == 2:
                    if event.key == pygame.K_F1:
                        self.hud_show = not self.hud_show

                if self.hud_id == 0 or self.hud_id == 1:
                    if event.key == pygame.K_UP:
                        if self.hudkeypos > 0:
                            self.hudkeypos -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.hudkeypos < 1:
                            self.hudkeypos += 1
                    elif event.key == pygame.K_RETURN:
                        if self.hud_id == 0:
                            if self.hudkeypos == 0:
                                self.hud_id = 2
                                self.hud_show = True
                            elif self.hudkeypos == 1:
                                self.hud_id = 1
                                self.hud_show = False
                        else:
                            if self.hudkeypos == 0:
                                exit()
                            elif self.hudkeypos == 1:
                                self.hud_id = 0

        # gameplay ui
        if self.hud_show:
            # + at center
            pygame.draw.line(self.screen, color.black, (hWIDTH, hHEIGHT - sep.height - sep.outline), (hWIDTH, hHEIGHT + sep.height + sep.outline), sep.size)
            pygame.draw.line(self.screen, color.black, (hWIDTH - sep.width - sep.outline, hHEIGHT), (hWIDTH + sep.width + sep.outline, hHEIGHT), sep.size)

            pygame.draw.line(self.screen, color.white, (hWIDTH, hHEIGHT - sep.height), (hWIDTH, hHEIGHT + sep.height), sep.size-sep.outline*2)
            pygame.draw.line(self.screen, color.white, (hWIDTH - sep.width, hHEIGHT), (hWIDTH + sep.width, hHEIGHT), sep.size-sep.outline*2)

            # fps & pos
            fps = str(int(clock.get_fps()))
            fps_view = self.font.render(fps, 0, color.red)
            pos_view = self.font.render('Position: ('+str(int(p_pos[0]))+', '+str(int(p_pos[1]))+')', 0, color.red)
            self.screen.blit(fps_view, (WIDTH-self.font.size(fps)[0], 0))
            self.screen.blit(pos_view, (5, 0))

            # minimap
            self.mapscreen.fill(color.black)

            mx, my = p_pos[0] // minimap.scale, p_pos[1] // minimap.scale

            pygame.draw.circle(self.mapscreen, color.red, (int(mx), int(my)), minimap.scale)
            pygame.draw.line(self.mapscreen, color.yellow, (mx, my),
                             (mx + WIDTH//100 * math.cos(p_angle), my + WIDTH//100 * math.sin(p_angle)), 2)

            for x, y in mmap:
                pygame.draw.rect(self.mapscreen, color.lightyellow, (x, y, minimap.tile, minimap.tile))

            self.screen.blit(self.mapscreen, minimap.pos)

        # main ui
        if self.hud_id == 0:
            pygame.mouse.set_visible(True)
            name_view = self.title.render(game.name, 0, color.green)
            name_size = self.font.size(game.name)
            self.screen.blit(name_view, (hWIDTH-name_size[0]*3.5, 0))

            start_button_text = (' '+self.buttons[0]+' ') if self.hudkeypos != 0 else ('>'+self.buttons[0]+'<')
            start_button = self.defolt.render(start_button_text, 0, color.blue)
            start_button_size = self.font.size(game.name)
            self.screen.blit(start_button, (hWIDTH, hHEIGHT-name_size[1]-10))

            exit_button_text = (' '+self.buttons[1]+' ') if self.hudkeypos != 1 else ('>' + self.buttons[1] + '<')
            exit_button = self.defolt.render(exit_button_text, 0, color.blue)
            self.screen.blit(exit_button, (hWIDTH, hHEIGHT + name_size[1] - start_button_size[1] + 20))
        elif self.hud_id == 1:
            pygame.mouse.set_visible(True)
            name_text = 'Do you want to exit?'
            name_view = self.defolt.render(name_text, 0, color.red)
            name_size = self.font.size(name_text)
            self.screen.blit(name_view, (hWIDTH-name_size[0], hHEIGHT-100))

            start_button_text = (' ' + self.buttons[2] + ' ') if self.hudkeypos != 0 else (
                        '>' + self.buttons[2] + '<')
            start_button = self.defolt.render(start_button_text, 0, color.blue)
            start_button_size = self.font.size(game.name)
            self.screen.blit(start_button, (hWIDTH, hHEIGHT - name_size[1] - 10))

            exit_button_text = (' ' + self.buttons[3] + ' ') if self.hudkeypos != 1 else (
                        '>' + self.buttons[3] + '<')
            exit_button = self.defolt.render(exit_button_text, 0, color.blue)
            self.screen.blit(exit_button, (hWIDTH, hHEIGHT + name_size[1] - start_button_size[1] + 20))
        else:
            pygame.mouse.set_visible(False)

        return self.hud_id

    def tiles(self, p_pos, p_angle):
        ox, oy = p_pos
        xm, ym = mapping(ox, oy)
        cur_angle = p_angle - ray.hfov
        for iray in range(ray.count):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)
            sin_a = sin_a if sin_a else 0.000001
            cos_a = cos_a if cos_a else 0.000001

            # verticals
            x, dx = (xm + tile.size, 1) if cos_a >= 0 else (xm, -1)
            for i in range(0, WIDTH, tile.size):
                depth_v = (x - ox) / cos_a
                yv = oy + depth_v * sin_a
                tile_v = mapping(x + dx, yv)
                if tile_v in wmap:
                    texture_v = wmap[tile_v]
                    break
                x += dx * tile.size

            # horizontals
            y, dy = (ym + tile.size, 1) if sin_a >= 0 else (ym, -1)
            for i in range(0, HEIGHT, tile.size):
                depth_h = (y - oy) / sin_a
                xh = ox + depth_h * cos_a
                tile_h = mapping(xh, y + dy)
                if tile_h in wmap:
                    texture_h = wmap[tile_h]
                    break
                y += dy * tile.size

            # projection
            depth, off, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
            off = int(off) % tile.size
            depth *= math.cos(p_angle - cur_angle)
            depth = max(depth, 0.00001)
            proj_height = min(int(ray.coef / depth), 2 * HEIGHT)

            wall_column = self.textures[texture].subsurface(off * textures.scale, 0, textures.scale, textures.height)
            wall_column = pygame.transform.scale(wall_column, (textures.scale, proj_height))
            self.screen.blit(wall_column, (iray * textures.scale, hHEIGHT - proj_height // 2))

            '''c = 255 / (1 + depth * depth * 0.00002)
            clr = (c, c // 2, c // 3)
            pygame.draw.rect(self.screen, clr,
                             (iray * ray.scale, hHEIGHT - proj_height // 2, ray.scale, proj_height))'''
            cur_angle += delta.angle