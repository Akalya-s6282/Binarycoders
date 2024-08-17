import os
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunt")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Treasure settings
treasure_size = 30
treasure_pos = [random.randint(0, WIDTH - treasure_size), random.randint(0, HEIGHT - treasure_size)]

# Game loop flag
game_over = False

# Set clock for controlling the frame rate
clock = pygame.time.Clock()

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    # Check for collision with treasure
    if (player_pos[0] < treasure_pos[0] < player_pos[0] + player_size or
        player_pos[0] < treasure_pos[0] + treasure_size < player_pos[0] + player_size) and \
       (player_pos[1] < treasure_pos[1] < player_pos[1] + player_size or
        player_pos[1] < treasure_pos[1] + treasure_size < player_pos[1] + player_size):
        print("Treasure found!")
        game_over = True

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player and treasure
    pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, GOLD, (treasure_pos[0], treasure_pos[1], treasure_size, treasure_size))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()