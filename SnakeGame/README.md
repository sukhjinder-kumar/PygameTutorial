## Introduction

To install pygame: `pip3 install pygame`

Before we begin the particulars, the basic game loop looks like -

```py
while running:
    events()  # Inputs like quit, up and down, etc
    loop()  # update game states like enemy position, health, etc
    render()  # render the new game states
```

## Getting Started

- First we initialize the pygame using `pygame.init()`. 

- We create canvas using `pygame.display.set_mode((width, height))`, assign it to a variable, as we reference it later (for example while drawing).

- To set title of the window (canvas), use `pygame.display.set_caption("<Title>")`.

- We also use `pygame.time.Clock()`, assign it to a var too (say `clock`). Used to monitor and control fps. Adds delay if more fps (~while loops). `clock.tick(fps)` at end of while loop. Also provides the time from last frame (which it added), can be useful in physics simulation.

- Following piece of code is obvious, and used for taking in input:

```py
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False  # Game loop stops
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("up arrow key pressed")
        elif event.key == pygame.K_DOWN:
            print("Down arrow key pressed")
        elif event.key == pygame.K_LEFT:
            print("Left arrow key pressed")
        elif event.key == pygame.K_RIGHT:
            print("Right arrow key pressed")
```

## Drawing in pygame

- Note: All below operation don't by themselves render, rather update the screen state. To render the new screen state use `pygame.display.flip()` in the end.

- Fill the entire screen with the same color: `screen.fill(color)`, where color is the hex tuple. Like (0, 0, 0) or (255, 255, 255) for black and white respectively.

- Line: `pygame.draw.line(screen, color, start_pos, end_pos, width)`

- Rectangle: `pygame.draw.rect(screen, color, rect, width=0)`, where rect attribute is (x, y, width, height) or a pygame.Rect object.

- Circle: `pygame.draw.circle(screen, color, center, radius, width=0)`

- Polygon: `pygame.draw.polygon(screen, color, pointlist, width=0)`, where pointlist is list of points (tuples)
