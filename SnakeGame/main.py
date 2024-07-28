import pygame

# pygame setup
pygame.init() 
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

# Define colors
BACKGROUND_COLOR = (0, 0, 0)  # Black
WHITE = (255, 255, 255)

# Basic game loop
#
# while True:
#     events() -- Inputs like quit, up and down, etc
#     loop() -- update game states like enemy position, health, etc
#     render() -- render the new game state

while running:
    # Events()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up arrow key pressed")
            elif event.key == pygame.K_DOWN:
                print("Down arrow key pressed")
            elif event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")

    # Learning to draw
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, WHITE, (10,5), (50,10), width=4)
    pygame.draw.rect(screen, WHITE, (10, 20, 40, 10), width=4)

    pygame.display.flip()

    # Loop()

    # render

pygame.quit() # Clean up
