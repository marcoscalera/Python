import pygame
from settings import *
from map import world_map

def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - half_fov
    xo, yo = player_pos
    for ray in range(num_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        for depth in range(max_depth):
            x = xo + depth * cos_a
            y = yo + depth * sin_a

            # verifica se o raio atingiu uma parede
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                proj_height = proj_coeff / (depth + 1e-5)  # evita divisão por zero
                wall_color = (max(0, 220 - depth // 3), 0, 0)  #cor da parede
                pygame.draw.rect(sc, wall_color, (ray * scale, half_height - proj_height // 2, scale, proj_height))
                break

        cur_angle += delta_angle