import pygame
import random

# Set up the game screen
pygame.init()
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Set up the game objects
ball_size = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = random.choice([-5, 5])
ball_speed_y = random.choice([-5, 5])
paddle_width = 10
paddle_height = 50
paddle_speed = 5
player1_score = 0
player2_score = 0

# Draw the game objects
def draw_ball(x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, ball_size, ball_size))

def draw_paddle(x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, paddle_width, paddle_height))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collisions with the walls
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1
    if ball_x <= 0:
        ball_speed_x *= -1
        player2_score += 1
    if ball_x >= screen_width - ball_size:
        ball_speed_x *= -1
        player1_score += 1

    # Check for collisions with the paddles
    if ball_x <= paddle_width and ball_y >= player1_y and ball_y <= player1_y + paddle_height:
        ball_speed_x *= -1
    if ball_x >= screen_width - paddle_width - ball_size and ball_y >= player2_y and ball_y <= player2_y + paddle_height:
        ball_speed_x *= -1

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += paddle_speed

    # Draw the game objects
    screen.fill((0, 0, 0))
    draw_ball(ball_x, ball_y)
    draw_paddle(0, player1_y)
    draw_paddle(screen_width - paddle_width, player2_y)
    pygame.display.update()

# Clean up
pygame.quit()
