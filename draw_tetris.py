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


    def draw_grid(self, grid):
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                color = cell if isinstance(cell, tuple) else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (x * self.block_size, y * self.block_size, self.block_size, self.block_size), 0)
                pygame.draw.rect(self.screen, (128, 128, 128), (x * self.block_size, y * self.block_size, self.block_size, self.block_size), 1)

    def draw_current_piece(self, game_instance):
            for y, row in enumerate(game_instance.current_piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, game_instance.current_piece.color, (game_instance.current_piece.x * self.block_size + x * self.block_size, game_instance.current_piece.y * self.block_size + y * self.block_size, self.block_size, self.block_size), 0)


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

    def clock(self): 
        return pygame.time.Clock()

            
