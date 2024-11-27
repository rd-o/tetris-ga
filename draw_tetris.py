import pygame

class DrawTetris:
    def __init__(self, screen_width, screen_height, block_size):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Tetris")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        # Load splash screen image
        self.splash_image = pygame.image.load('tetris.png')
        self.font = pygame.font.Font('DepartureMono-Regular.otf', 20)
        self.clock = pygame.time.Clock()

    def index_to_coordinates(self, index, width):
        x = index % width
        y = index // width
        return x, y

#    def draw_grid(self, grid, draw_index):
#        for y, row in enumerate(grid):
#            for x, cell in enumerate(row):
#                color = cell if isinstance(cell, tuple) else (0, 0, 0)
#                pygame.draw.rect(self.screen, color, (x * self.block_size, y * self.block_size, self.block_size, self.block_size), 0)
#                pygame.draw.rect(self.screen, (128, 128, 128), (x * self.block_size, y * self.block_size, self.block_size, self.block_size), 1)

    def draw_grid(self, grid, draw_index):
        """
        Draws a grid at a specific position determined by draw_index.

        :param grid: The grid data (2D list) to be drawn.
        :param draw_index: The index determining the grid's position on the screen.
        """

        x_start, y_start = self.calculate_coord_start(grid, draw_index)

        # Draw the grid at the calculated position
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                color = cell if isinstance(cell, tuple) else (0, 0, 0)  # Default to black if not a tuple
                rect = (x_start + x * self.block_size, y_start + y * self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, color, rect, 0)  # Draw cell
                pygame.draw.rect(self.screen, (128, 128, 128), rect, 1)  # Draw grid outline

#    def draw_current_piece(self, game_instance, draw_index):
#            for y, row in enumerate(game_instance.current_piece.shape):
#                for x, cell in enumerate(row):
#                    if cell:
#                        pygame.draw.rect(self.screen, game_instance.current_piece.color, (game_instance.current_piece.x * self.block_size + x * self.block_size, game_instance.current_piece.y * self.block_size + y * self.block_size, self.block_size, self.block_size), 0)
    def calculate_coord_start(self, grid, draw_index):
        # Determine grid position based on draw_index
        cols_per_screen = self.screen.get_width() // (len(grid[0]) * self.block_size)
        x_offset, y_offset = self.index_to_coordinates(draw_index, cols_per_screen)

        # Calculate top-left corner of the grid
        x_start = x_offset * len(grid[0]) * self.block_size
        y_start = y_offset * len(grid) * self.block_size

        return x_start, y_start

    def draw_current_piece(self, game_instance, draw_index):
        """
        Draws the current piece of a Tetris game at a position determined by draw_index.

        :param game_instance: The game instance containing the current piece.
        :param draw_index: The index determining the position of the game on the screen.
        """
        # Determine grid position based on draw_index
        #cols_per_screen = self.screen.get_width() // (len(game_instance.grid[0]) * self.block_size)
        #x_offset, y_offset = self.index_to_coordinates(draw_index, cols_per_screen)

        # Calculate top-left corner of the grid
        #x_start = x_offset * game_instance.grid_width * self.block_size
        #y_start = y_offset * game_instance.grid_height * self.block_size

        x_start, y_start = self.calculate_coord_start(game_instance.grid, draw_index)

        # Draw the current piece at the calculated position
        for y, row in enumerate(game_instance.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = (
                        x_start + (game_instance.current_piece.x + x) * self.block_size,
                        y_start + (game_instance.current_piece.y + y) * self.block_size,
                        self.block_size,
                        self.block_size,
                    )
                    pygame.draw.rect(self.screen, game_instance.current_piece.color, rect, 0)



    def draw_splash_screen(self):
        self.screen.fill((0, 0, 0))  # Fill background with black before blitting the image
        splash_rect = self.splash_image.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(self.splash_image, splash_rect)
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        label = self.font.render(text, 1, color)
        self.screen.blit(label, (x, y))

    def exit(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black before showing "Game Over"
        self.draw_text("Game Over", 60, (255, 0, 0), self.screen_width // 2 - 150, self.screen_height // 2 - 30)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

    def key_events(self, game_instance):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_instance.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game_instance.move_piece_left()
                if event.key == pygame.K_d:
                    game_instance.move_piece_right()
                if event.key == pygame.K_s:
                    game_instance.move_piece_down()
                if event.key == pygame.K_w:
                    game_instance.rotate_piece()


    def update(self):
        pygame.display.update()

    #def get_clock(self):
    #    return self.

    #def get_free_space():
        

            
