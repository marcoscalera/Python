import pygame
from settings import *
from player import Player
from ray_casting import ray_casting
from map import world_map

pygame.init()
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo 3D - Marcos Paulo Calera")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)  # fonte para o contador de FPS

player = Player()

# superficie renderização
game_surface = pygame.Surface((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # movimentacao do jogador
    player.movement()

    # rendderizacao intermediária
    game_surface.fill(black)

    # desenha o chão e o teto
    pygame.draw.rect(game_surface, floor_color, (0, half_height, width, half_height))
    pygame.draw.rect(game_surface, ceiling_color, (0, 0, width, half_height))

    #ray casting
    ray_casting(game_surface, player.pos, player.angle)

    # contador de FPS
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, white)
    game_surface.blit(fps_text, (10, 10))

    # desenha a superfície na tela
    sc.blit(game_surface, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)