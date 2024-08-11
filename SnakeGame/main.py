import pygame
import random 

# Define colors
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
BACKGROUND_COLOR = (0, 0, 0)  # black
GRID_COLOR = (255, 255, 255)  # white
SNAKE_COLOR = (255, 255, 255)  # --
FOOD_COLOR = (255, 0, 0)  # red
GRID_WIDTH = 20
GRID_HEIGHT = 20
NUM_GRID_COL = DISPLAY_WIDTH // GRID_WIDTH
NUM_GRID_ROW = DISPLAY_HEIGHT // GRID_HEIGHT

# pygame setup
pygame.init() 
screen = pygame.display.set_mode((DISPLAY_HEIGHT, DISPLAY_WIDTH))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # None means using the default font, 36 is the size
running = 1

def draw_grid():
    for x in range(0,DISPLAY_WIDTH, GRID_WIDTH):
        pygame.draw.line(screen, GRID_COLOR, [x,0], [x,DISPLAY_HEIGHT], width=1)
    for y in range(0,DISPLAY_HEIGHT, GRID_HEIGHT):
        pygame.draw.line(screen, GRID_COLOR, [0,y], [DISPLAY_WIDTH,y], width=1)

def color_rect(x, y, color):
    rect = [x*GRID_WIDTH+1, y*GRID_HEIGHT+1, GRID_WIDTH-1, GRID_HEIGHT-1]
    pygame.draw.rect(screen, color, rect, width=0)


class Snake:
    def __init__(self, pointlist=None):
        if pointlist == None:
            # Don't make the NUM_GRID_[row or col] < 3
            middle = [NUM_GRID_COL // 2, NUM_GRID_ROW // 2]
            left = [NUM_GRID_COL // 2 - 1, NUM_GRID_ROW // 2]
            right = [NUM_GRID_COL // 2 + 1, NUM_GRID_ROW // 2]
            self.pointlist = [left, middle, right]
        else:
            self.pointlist = pointlist  # [[x,y]]: starting with tail and ending with head
        self.length = len(self.pointlist)
        self.direction = [1,0]  # [i, j]: [1,0], [-1,0], [0,1], [0,-1]

    def valid_snake(self):
        # check if direction is our of four only
        if self.direction not in [[1,0], [-1,0], [0,1], [0,-1]]:
            print("Direction wrong!")
            return 0
        # check if pointlist makes sense
        for i in range(len(self.pointlist) - 2):
            if abs(self.pointlist[i][0] - self.pointlist[i+1][0]) \
                + abs(self.pointlist[i][1] - self.pointlist[i+1][1]) != 1:
                print('Pointlist is not "linear"')
                return 0
        # check collision with itself
        def repeat_exist(list_point):
            seen = set() 
            repeat = set() 
            for point in list_point:
                tuple_point = tuple(point)
                if tuple_point in seen:
                    repeat.add(tuple_point)
                else:
                    seen.add(tuple_point)
            return 0 if len(repeat) == 0 else 1
        if repeat_exist(self.pointlist):
            print("Collision detected")
            return 0
        # check collision with the wall
        head = self.pointlist[len(self.pointlist) - 1]
        if head[0] < 0 or head[0] > NUM_GRID_COL - 1 or \
            head[1] < 0 or head[1] > NUM_GRID_ROW - 1:
            print("Collision with the wall")
            return 0
        # return 1 if all checks are fine 
        return 1

    def move_snake(self):
        # move the snake in direction one step. 
        old_head = self.pointlist[len(self.pointlist)-1]
        new_head = [old_head[0] + self.direction[0], old_head[1] + self.direction[1]]
        self.pointlist = self.pointlist[1:len(self.pointlist)]
        self.pointlist.append(new_head)

    def inc_length(self):
        # called when snake ate food and want to increase length
        # a new cell (new tail) is added
        tail_direction = [self.pointlist[0][0] - self.pointlist[1][0], \
                          self.pointlist[0][1] - self.pointlist[1][1]]
        new_tail = [self.pointlist[0][0] + tail_direction[0], self.pointlist[0][1] + tail_direction[1]]
        if not (new_tail[0] < 0 or new_tail[0] > NUM_GRID_COL - 1 or \
            new_tail[1] < 0 or new_tail[1] > NUM_GRID_ROW):
            self.pointlist.insert(0, new_tail)
        else:
            # increase length some other way
            pass


class Food:
    def __init__(self, location=None, point=1):
        if location == None:
            self.location = [NUM_GRID_COL // 2 + 3, NUM_GRID_ROW // 2]
        else:
            self.location = location
        self.point = point  # value of each food
    def new_location(self, snake_pointlist):
        def pdf(pointlist):
            return [1/len(pointlist)]*len(pointlist) 
        grid = [[x,y] for x in range(NUM_GRID_COL) for y in range(NUM_GRID_ROW)]
        grid_minus_snake_pointlist = [element for element in grid \
            if element not in snake_pointlist]
        self.location = random.choices(grid_minus_snake_pointlist, \
                                      pdf(grid_minus_snake_pointlist), \
                                      k=1)[0]


class GameState:
    def __init__(self, def_snake=Snake(), def_food=Food()):
        self.snake = def_snake
        self.food = def_food
        self.score = 0

    def update_game_state(self):
        # The user can only update the direction of snake 
        # returns not_over (0 or 1)
        # 1. Move the snake
        self.snake.move_snake()
        # 2. Check if snake is colliding with itself or the wall
        is_valid = self.snake.valid_snake()
        # 3. Check if snake head is on food. If yes increase length of snake and update food
        if self.snake.pointlist[len(self.snake.pointlist)-1] == self.food.location:
            self.snake.inc_length()
            self.score += 1
            self.food.new_location(self.snake.pointlist)
        return is_valid

    def render_game_state(self, show_grid=True):
        # Set background color
        screen.fill(BACKGROUND_COLOR)
        # Draw grid
        if show_grid:
            draw_grid()
        # show snake 
        for cell in self.snake.pointlist:
            color_rect(cell[0], cell[1], SNAKE_COLOR)
        # show food
        color_rect(self.food.location[0], self.food.location[1], FOOD_COLOR)
        # show score
        text_surface = font.render(f"Score:{self.score}", True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=(50,50))  # Center of the screen
        screen.blit(text_surface, text_rect)

        pygame.display.flip()


game_state = GameState()
fps = 10

while running:
    # Events()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # print("up arrow key pressed")
                game_state.snake.direction = [0,-1]
            elif event.key == pygame.K_DOWN:
                # print("Down arrow key pressed")
                game_state.snake.direction = [0,1]
            elif event.key == pygame.K_LEFT:
                # print("Left arrow key pressed")
                game_state.snake.direction = [-1,0]
            elif event.key == pygame.K_RIGHT:
                # print("Right arrow key pressed")
                game_state.snake.direction = [1,0]

    # Loop
    running = game_state.update_game_state()

    if running == 1:
        # Render
        game_state.render_game_state(show_grid=False)

        # Delay for fps
        clock.tick(fps)

print(f"{game_state.score}")
pygame.quit()  # clean up
print("Hope you enjoyed the snake game")
