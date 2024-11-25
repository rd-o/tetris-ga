from tetris_game import TetrisGame
from draw_tetris import DrawTetris  

# Screen dimensions
screen_width = 300
screen_height = 600
block_size = 30

# Game variables
fall_time = 0
score = 0
draw_tetris_instance = DrawTetris(screen_width, screen_height, block_size)
clock = draw_tetris_instance.clock()

def main():
    #global grid, score
    
    run = True
    #fall_speed = 0.27
    #fall_time = 0

    #draw_tetris_instance.draw_splash_screen()

    game_instance = TetrisGame(screen_width // block_size, screen_height // block_size)
    game_instance.setup_pygame()

    while run:
        run = game_instance.update_with_graphics()
#        grid = game_instance.create_grid()
#        fall_time += clock.get_rawtime()
#        clock.tick()
#
#        if fall_time / 1000 >= fall_speed:
#            fall_time = 0
#            run = game_instance.update_game_state()
#
#        run = draw_tetris_instance.key_events(game_instance)
#
#        draw_tetris_instance.draw_grid(grid)
#        draw_tetris_instance.draw_current_piece(game_instance)
#        
#        score = game_instance.calculate_score()
#        draw_tetris_instance.draw_text(f"Score: {score}", 30, (255, 255, 255), 10, 10)
#        #clear_rows(grid, game_instance.locked_positions)
#        draw_tetris_instance.update()

    draw_tetris_instance.exit()

main()
