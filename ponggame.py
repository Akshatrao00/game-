import pygame

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Screen size
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game by Bhai")

# Paddle properties
paddle_width, paddle_height = 10, 70
paddle_speed = 7

# Ball properties
ball_size = 15
ball_speed_x = 5
ball_speed_y = 5

# Player positions
player1_y = height // 2 - paddle_height // 2
player2_y = height // 2 - paddle_height // 2
player1_score = 0
player2_score = 0

# Ball position
ball_x = width // 2 - ball_size // 2
ball_y = height // 2 - ball_size // 2

# Font
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(black)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < height - paddle_height:
        player2_y += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top/bottom
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= paddle_width and player1_y < ball_y < player1_y + paddle_height):
        ball_speed_x *= -1
    if (ball_x >= width - paddle_width - ball_size and player2_y < ball_y < player2_y + paddle_height):
        ball_speed_x *= -1

    # Score update
    if ball_x < 0:
        player2_score += 1
        ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
    if ball_x > width:
        player1_score += 1
        ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2

    # Draw paddles
    pygame.draw.rect(screen, white, (0, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (width - paddle_width, player2_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Draw scores
    score_text = font.render(f"{player1_score} : {player2_score}", True, white)
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
