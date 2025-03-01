import math

# configurações básicas
width = 1200
height = 800

half_width = width // 2
half_height = height // 2

FPS = 60
TILE = 100  
FOV = math.pi / 3 

half_fov = FOV / 2
num_rays = 60  
max_depth = 800
delta_angle = FOV / num_rays
dist = num_rays / (2 * math.tan(half_fov))
proj_coeff = dist * TILE
scale = width // num_rays

# jogador
player_pos = (half_width, half_height)
player_angle = 0
player_speed = 1 

# cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 0, 0)
green = (0, 220, 0)
blue = (0, 0, 220)
gray = (110, 110, 110)
purple = (120, 0, 120)
floor_color = gray  
ceiling_color = (80, 80, 80)  