from draw_tetris import DrawTetris  
from tetris_game import TetrisGame


screen_width = 600
screen_height = 600
block_size = 10
if __name__ == "__main__":
    draw_tetris_instance = DrawTetris(screen_width, screen_height, block_size)
    tetris_game1 = TetrisGame(10, 20)
    tetris_game2 = TetrisGame(10, 20)
    tetris_game1.setup_instance(draw_tetris_instance, 0)
    tetris_game2.setup_instance(draw_tetris_instance, 1)
    #grid = tetris_game.create_grid()

    
    #tetris_game.update_with_multiple_graphics(draw_tetris_instance, 0)

    run = True
    while run:
        tetris_game1.update_with_multiple_graphics()
        tetris_game2.update_with_multiple_graphics()

