from settings import *

# mapa em formato de texto
text_map = [
    'WWWWWWWWWWWW',
    'W....WW....W',
    'W....WWW...W',
    'W.WW.......W',
    'WW......WWW',
    'WWW........W',
    'W.......W..W',
    'WWWWWWWWWWWW'
]

# converte o mapa de texto para coordenadas no mundo
world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))