import pygame
import sys
import math
import random

WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
SUN_COLOR = (255, 255, 0)
FLARE_COLOR = (255, 0, 0)
FLARE_RADIUS = 10
FLARE_INTENSITY = 10
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar Flare")
clock = pygame.time.Clock()

def calculate_position(center, radius, angle):
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    return int(x), int(y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    sun_center = (WIDTH // 2, HEIGHT // 2)
    pygame.draw.circle(screen, SUN_COLOR, sun_center, 50)
    for _ in range(FLARE_INTENSITY):
        flare_angle = random.uniform(0, 2 * math.pi)
        flare_position = calculate_position(sun_center, 50, flare_angle)
        pygame.draw.circle(screen, FLARE_COLOR, flare_position, FLARE_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
