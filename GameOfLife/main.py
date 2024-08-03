# For variables, function use snake_case (all small letters)
# For classes, use CamelCase
# For constants, Use SNAKE_CASE (all capital letters)

import pygame
import copy

DISPLAY_WIDTH = 501
DISPLAY_HEIGHT = 501
GRID_WIDTH = 10  # Could be > DISPLAY_WIDTH too, no boundary game state
GRID_HEIGHT = 10 
NUM_GRID_X = DISPLAY_WIDTH // GRID_WIDTH  # = 20
NUM_GRID_Y = DISPLAY_HEIGHT // GRID_HEIGHT
BACKGROUND_COLOR = (0, 0, 0)  # black
CELL_COLOR = (255, 0, 0)  # red
GRID_COLOR = (255, 255, 255) # white

# setup pygame
pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
running = True


# Draw grid
def draw_grid():
    for x in range(0,DISPLAY_WIDTH, GRID_WIDTH):
        pygame.draw.line(screen, GRID_COLOR, [x,0], [x,DISPLAY_HEIGHT], width=1)
    for y in range(0,DISPLAY_HEIGHT, GRID_HEIGHT):
        pygame.draw.line(screen, GRID_COLOR, [0,y], [DISPLAY_WIDTH,y], width=1)

def color_rect(i, j):
    rect = [j*GRID_WIDTH+1, i*GRID_HEIGHT+1, GRID_WIDTH-1, GRID_HEIGHT-1]
    pygame.draw.rect(screen, CELL_COLOR, rect, width=0)

def uncolor_rect(i, j):
    rect = [j*GRID_WIDTH+1, i*GRID_HEIGHT+1, GRID_WIDTH-1, GRID_HEIGHT-1]
    pygame.draw.rect(screen, BACKGROUND_COLOR, rect, width=0)

# Define game of life state
class GameState():

    def __init__(self, init_cell_state=None):
        if init_cell_state == None:
            self.cell_state = self.init_cell_state()
        else:
            self.cell_state = init_cell_state
        self.generation = 1
        self.count_alive = self.count_alive_cell()

    def init_cell_state(self):
        row = [0]*NUM_GRID_X
        grid = [row[:] for _ in range(NUM_GRID_Y)]  # created a 2d array of size NUM_GRID_Y x NUM_GRID_X, all 0
        # init_coordinate = [NUM_GRID_Y // 2, NUM_GRID_X // 2]
        # grid[init_coordinate[0]][init_coordinate[1]] = 1
        # grid[NUM_GRID_Y - 1][NUM_GRID_X - 1] = 1

        # grid selector
        screen.fill(BACKGROUND_COLOR)
        draw_grid()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # enter key
                        running = False
                        print("Enter key pressed")
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left mouse button
                        i = event.pos[1] // GRID_HEIGHT
                        j = event.pos[0] // GRID_WIDTH
                        # print(f'{i}, {j} grid value inversed')
                        if grid[i][j] == 0:
                            grid[i][j] = 1
                            color_rect(i, j)
                        else:
                            grid[i][j] = 0
                            uncolor_rect(i, j)
            pygame.display.flip()
        return grid

    def count_alive_cell(self):
        count = 0
        for i in range(NUM_GRID_Y):
            for j in range(NUM_GRID_X):
                if self.cell_state[i][j] == 1:
                    count += 1
        return count

    def count_alive_neightbor(self, i, j):
        count = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                elif j + x > NUM_GRID_X - 1 or j + x < 0 or i + y > NUM_GRID_Y - 1 or i + y < 0:
                    continue
                elif self.cell_state[i+y][j+x] == 1:
                    count += 1
        return count

    def update_game_state(self):
        # update rule
        new_grid = copy.deepcopy(self.cell_state)
        for i in range(NUM_GRID_Y):
            for j in range(NUM_GRID_X):
                if (self.cell_state[i][j] == 1 and (self.count_alive_neightbor(i, j) < 2
                    or self.count_alive_neightbor(i, j) > 3)):
                    new_grid[i][j] = 0
                if self.cell_state[i][j] == 0 and self.count_alive_neightbor(i, j) == 3:
                    new_grid[i][j] = 1
        self.cell_state = new_grid

        self.generation += 1
        self.count_alive = self.count_alive_cell()

    def game_state_render(self, show_grid=False):
        # Set background color
        screen.fill(BACKGROUND_COLOR)

        # Draw grid
        if show_grid:
            draw_grid()

        # Mark alive cells
        for i in range(0, NUM_GRID_Y):
            for j in range(0, NUM_GRID_X):
                if self.cell_state[i][j] == 1:
                    color_rect(i, j)

        pygame.display.flip()


game_state = GameState()
fps = 10

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Loop
    game_state.update_game_state()

    # Render
    game_state.game_state_render()

    # Delay for fps
    clock.tick(fps)

pygame.quit()
print("Hope you enjoyed the game of life demo")
