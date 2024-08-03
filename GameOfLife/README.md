## Conway's Game of Life - Pygame Implementation

This script provides a graphical implementation of Conway's Game of Life using Pygame. It allows users to interactively set the initial state of the grid and observe the evolution of the game through successive generations.

1. Install the dependencies and run by `python3 main.py`. 

2. First you have to select (or deselect) cells on grid which you want to make alive for the first generation. Press enter

3. By default, grid is not shown you can change that in code by providing `game_state.game_state_render(show_grid=True)`.

4. You can see the changing automata. Red cells are alive and black ones are dead. For now boundary condition is applied (ignored in calculation of alive cells), though game is set on infinite scale. We can, in future, either make the grid too large and make it scrollable or just keep grid_width and grid_hieght very less (can't be less than 1 though)

## Codebase

- We have created a general class called `GameState` which handles all the game related functions. First on initilization, `init_cell_state()` function is called (written inside of the class), which is responsible for handling of selecting and deselecting cells (step 2 in above).

- After initilization, to update the game_state, we have defined `game_state.update_game_state()` function.

- And finally to render it, we have defined `game_state.game_state_render()` function. Which takes in a param `show_grid` which tells if to show or hide the grid view.

## Documentation (by ChatGPT)

### Constants

- `DISPLAY_WIDTH`: Width of the display window in pixels. (501)
- `DISPLAY_HEIGHT`: Height of the display window in pixels. (501)
- `GRID_WIDTH`: Width of each grid cell in pixels. (10)
- `GRID_HEIGHT`: Height of each grid cell in pixels. (10)
- `NUM_GRID_X`: Number of horizontal cells in the grid. (`DISPLAY_WIDTH // GRID_WIDTH`)
- `NUM_GRID_Y`: Number of vertical cells in the grid. (`DISPLAY_HEIGHT // GRID_HEIGHT`)
- `BACKGROUND_COLOR`: RGB color value for the background. (Black: `(0, 0, 0)`)
- `CELL_COLOR`: RGB color value for alive cells. (Red: `(255, 0, 0)`)
- `GRID_COLOR`: RGB color value for the grid lines. (White: `(255, 255, 255)`)

### Initialization

1. **Pygame Setup**: Initializes Pygame and sets up the display window with the given dimensions.
2. **Display Settings**: Sets the window caption and creates a clock object to control the frame rate.

### Functions

#### `draw_grid()`
Draws the grid lines on the display.

#### `color_rect(i, j)`
Colors a specific grid cell at position `(i, j)` with the cell color.

#### `uncolor_rect(i, j)`
Removes the color from a specific grid cell at position `(i, j)` by filling it with the background color.

### Classes

#### `GameState`

##### Methods

- **`__init__(self, init_cell_state=None)`**
  Initializes the game state. If `init_cell_state` is provided, it sets the grid to that state. Otherwise, it initializes a blank grid and waits for user input to set the initial state.

- **`init_cell_state(self)`**
  Initializes the cell state with a 2D array of zeros. Allows the user to set the initial configuration of cells by clicking on the grid.

- **`count_alive_cell(self)`**
  Counts and returns the number of alive cells in the grid.

- **`count_alive_neightbor(self, i, j)`**
  Counts and returns the number of alive neighbors around the cell at position `(i, j)`.

- **`update_game_state(self)`**
  Updates the game state based on the rules of Conway's Game of Life. Creates a new grid based on the current state and the number of alive neighbors.

- **`game_state_render(self, show_grid=False)`**
  Renders the current game state on the display. Optionally draws the grid lines if `show_grid` is set to `True`.

### Main Loop

1. **Event Handling**: Handles user events such as quitting the game.
2. **Game Update**: Updates the game state for each frame.
3. **Rendering**: Renders the updated game state on the display.
4. **Frame Rate Control**: Controls the frame rate of the game using the clock object.

### Running the Game

The game runs in a loop where it updates the game state and renders the grid at each frame. The game will continue running until the user closes the window.

