import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Ball dimensions
BALL_SIZE = 10

# Paddle speeds
PADDLE_SPEED = 7

# Ball speed
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Scores
score_left = 0
score_right = 0

# Fonts
font = pygame.font.Font(None, 74)

# Clock
clock = pygame.time.Clock()
# Paddles
paddle_left = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_right = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    # Paddle movement
    if keys[pygame.K_w] and paddle_left.top > 0:
        paddle_left.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_left.bottom < HEIGHT:
        paddle_left.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_right.top > 0:
        paddle_right.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_right.bottom < HEIGHT:
        paddle_right.y += PADDLE_SPEED
    
    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    # Ball collision with paddles
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_speed_x *= -1
    
    # Scoring
    if ball.left <= 0:
        score_right += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = BALL_SPEED_X * random.choice((-1, 1))
        ball_speed_y = BALL_SPEED_Y * random.choice((-1, 1))
    if ball.right >= WIDTH:
        score_left += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = BALL_SPEED_X * random.choice((-1, 1))
        ball_speed_y = BALL_SPEED_Y * random.choice((-1, 1))
    
    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_left)
    pygame.draw.rect(screen, WHITE, paddle_right)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    text_left = font.render(str(score_left), True, WHITE)
    text_right = font.render(str(score_right), True, WHITE)
    screen.blit(text_left, (WIDTH // 4 - text_left.get_width() // 2, 20))
    screen.blit(text_right, (3 * WIDTH // 4 - text_right.get_width() // 2, 20))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
