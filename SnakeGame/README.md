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

## Snake Game

- First let us start with the game state. 

    - Description of snake: The entire length of snake, its tail and head, direction of motion (after the event)

    - Description of food: loc of food ~ Probability distribution(grid - snake occupied). This is also after event, so if snake head coincide with food, the length increase and a new food location is given.

    - Score: number of food eaten.

- Update game state. Returns is_over, new game state.

    - is_over: If the snakes goes out of bound or touches itself or no more space to go game is over.

    - new game state: The position of entire snake is updated based on direction. If the snake lands on food, the length is increased (say the tail increase).

Technically we are writing -

```py

class Snake:
    def __init__(self, len=3, pointlist=(...)):
        self.pointlist = pointlist # starting with head and ending with tail
        self.length = len(pointlist)
        self.direction = (...) # (1,0), (-1,0), (0,1), (0,-1)
    def valid_snake(self):
        # check if pointlist makes sense
        # check if direction is our of four only
        # Also check collision with itself
        pass
    def move_snake(self):
        # move the snake in direction one step. 
        # update pointlist
        pass
    def inc_length(self):
        # called when snake ate food and want to increase length
        pass

class Food:
    def __init__(self, location=(...), point=1):
        self.location = (...)
        self.point = point
    def new_location(self, snake_pointlist):
        self.location = ~Probability(grid - snake_pointlist)


class GameState:
    def __init__(self, def_snake=Snake(), def_food=Food()):
        self.snake = def_snake
        self.food = def_food
        self.score = 0
    def update_gamestate(self):
        # The user can only update the direction of snake 
        # returns is_over (bool)
        # 1. Move the snake
        # 2. Check if snake is colliding with itself or the wall
        # 3. Check if snake head is on food. If yes increase length of snake and update food
        pass
    def render_gamestate(self):
        pass
```

- Now the snake also has some size (not just a pixel). Instead of using standard pygame co-ordinates, we transform the gridspace into a bigger grid space and above classes are coordinates in that grid space. So (x,y) in new grid space translates to (x*blockSize, y*blocksize) in orignial space (the co-ordinate of top left of the rect. But can treat as that of grid too!)

```py
def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
```
