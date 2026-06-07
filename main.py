import pygame

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((800, 600))  # width, height in pixels
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# --- Game Loop ---
running = True
while running:

    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game state
    # (move objects, check collisions, etc.)

    # 3. Draw
    screen.fill((0, 0, 0))  # fill background black (R, G, B)
    # draw your objects here

    pygame.display.flip()   # push drawn frame to screen

    # 4. Cap frame rate
    clock.tick(60)

pygame.quit()