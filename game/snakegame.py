import pygame
import time
import random

# Initialize Pygame
pygame.init()

# setting up how it would display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Snake block size
block_size = 20

# The speed of the snake 
snake_speed = 10

# Define margins to avoid placing apples on the borders, by the size of one block
border_margin = block_size  

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], block_size, block_size])

def generate_food():
    # Calculate the valid range for apple positions to avoid borders
    x_range = range(border_margin, width - border_margin, block_size)
    y_range = range(border_margin, height - border_margin, block_size)
    
    # Generate a random position within the valid range
    food_position = [
        random.choice(x_range),
        random.choice(y_range)
    ]
    return food_position

def display_score(score):
    font = pygame.font.SysFont(None, 35)
    value = font.render(f"Score: {score}", True, white)
    window.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width // 2
    y1 = height // 2

    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Initialize score
    score = 0

    # Generate the first food item
    food_position = generate_food()

    while not game_over:

        while game_close:
            window.fill(black)
            font = pygame.font.SysFont(None, 50)
            msg = font.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            window.blit(msg, [width // 6, height // 3])
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        # Draw the apple in red
        pygame.draw.rect(window, red, [food_position[0], food_position[1], block_size, block_size])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        our_snake(block_size, snake_list)
        display_score(score)  # Display the score

        pygame.display.update()

        if x1 == food_position[0] and y1 == food_position[1]:
            food_position = generate_food()
            length_of_snake += 1
            score += 1  # Increment score when the snake eats the apple

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
