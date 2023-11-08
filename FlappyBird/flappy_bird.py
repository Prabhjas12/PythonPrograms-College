import pygame
import sys
import random

# Initialize Pygame
pygame.init()
 
# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 40
BIRD_HEIGHT = 40
PIPE_WIDTH = 60
PIPE_HEIGHT = 300
PIPE_GAP = 200
PIPE_SPEED = 2
GRAVITY = 1
BIRD_JUMP = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Background
background = pygame.image.load("bg.jpg")

# Bird properties
bird_x = 100
bird_y = 250
bird_velocity = 0

# Pipe properties
pipe_x = SCREEN_WIDTH
pipe_height = [random.randint(300, 500) for _ in range(4)]
pipe_width = PIPE_WIDTH
pipe_distance = 300  # Adjust the initial pipe distance
pipe_speed = PIPE_SPEED

# Score
score = 0
font = pygame.font.Font(None, 36)

# Sounds
jump_sound = pygame.mixer.Sound("flap.mp3")
collision_sound = pygame.mixer.Sound("collision.mp3")

# Game state
game_over = False

def draw_objects():
    screen.blit(background, (0, 0))
    for i in range(4):
        pygame.draw.rect(screen, BLACK, (pipe_x, 0, pipe_width, pipe_height[i]))
        pygame.draw.rect(screen, BLACK, (pipe_x, pipe_height[i] + pipe_distance, pipe_width, SCREEN_HEIGHT))
    pygame.draw.rect(screen, BLACK, (bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT))
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

def game_over_screen():
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

def start_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to Jump", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

def restart_game():
    global bird_y, bird_velocity, pipe_x, pipe_height, score, game_over
    bird_y = 250
    bird_velocity = 0
    pipe_x = SCREEN_WIDTH
    pipe_height = [random.randint(100, 400) for _ in range(4)]
    score = 0
    game_over = False

# Load sounds
pygame.mixer.init()
jump_sound.set_volume(0.1)
collision_sound.set_volume(0.2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    bird_velocity = -BIRD_JUMP
                    jump_sound.play()
                elif game_over:
                    restart_game()

    if not game_over:
        # Bird physics
        bird_y += bird_velocity
        bird_velocity += GRAVITY

        # Pipe movement
        for i in range(4):
            pipe_x -= pipe_speed
            if pipe_x < -pipe_width:
                pipe_x = SCREEN_WIDTH
                pipe_height[i] = random.randint(100, 400)

            # Check for collisions
            if (
                bird_x + BIRD_WIDTH > pipe_x
                and bird_x < pipe_x + pipe_width
                and (bird_y < pipe_height[i] or bird_y + BIRD_HEIGHT > pipe_height[i] + pipe_distance)
            ):
                game_over = True
                collision_sound.play()

            # Increase score if bird passes a pipe
            if bird_x > pipe_x + pipe_width and bird_x < pipe_x + pipe_width + pipe_speed:
                score += 1

        # Game over if bird goes out of the screen
        if bird_y < 0 or bird_y > SCREEN_HEIGHT - BIRD_HEIGHT:
            game_over = True
            collision_sound.play()

    draw_objects()
    
    if game_over:
        game_over_screen()
    elif not game_over and bird_y < 0:
        start_screen()

    pygame.display.flip()
