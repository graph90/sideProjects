import pygame
import numpy as np
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
MAX_ITERATIONS = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Color Effects with Fractals")

def draw_mandelbrot(x_offset, y_offset, zoom):
    iteration_counts = np.zeros((HEIGHT, WIDTH), dtype=int)
    
    x = np.linspace(-2.0 / zoom + x_offset, 1.0 / zoom + x_offset, WIDTH)
    y = np.linspace(-1.5 / zoom + y_offset, 1.5 / zoom + y_offset, HEIGHT)
    X, Y = np.meshgrid(x, y)
    
    Z = X + 1j * Y
    C = Z.copy()

    mask = np.ones((HEIGHT, WIDTH), dtype=bool)

    for i in range(MAX_ITERATIONS):
        Z[mask] = Z[mask] ** 2 + C[mask]
        mask = np.abs(Z) <= 2
        iteration_counts[mask] += 1

    image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if iteration_counts[y, x] == MAX_ITERATIONS:
                color = (0, 0, 0)
            else:
                color = (iteration_counts[y, x] % 256, 
                         (iteration_counts[y, x] * 5) % 256, 
                         (iteration_counts[y, x] * 10) % 256)
            image[y, x] = color

    pygame_image = pygame.surfarray.make_surface(image)
    screen.blit(pygame_image, (0, 0))

def main():
    clock = pygame.time.Clock()
    x_offset, y_offset = 0, 0
    zoom = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        x_offset = (mouse_x / WIDTH - 0.5) * 4
        y_offset = (mouse_y / HEIGHT - 0.5) * 4

        screen.fill(BACKGROUND_COLOR)
        draw_mandelbrot(x_offset, y_offset, zoom)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
