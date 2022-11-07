import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
ORANGE = (237, 144, 43)
GREEN = (110, 208, 99)
RED = (230, 50, 52)
YELLOW = (245, 200, 53)
BLUE = (110, 190, 245)



# Creat the game loop
running = True 
while running: 
    # Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    # Draw a circle
    color = (255, 0, 255)
    position = (250, 250)
    pygame.draw.circle(screen, RED, (65, 65), 60)
    pygame.draw.circle(screen, ORANGE, (435, 65), 60)
    pygame.draw.circle(screen, YELLOW, position, 60)
    pygame.draw.circle(screen, GREEN, (65, 435), 60)
    pygame.draw.circle(screen, BLUE, (435, 435), 60)
    # Update the display
    pygame.display.flip()