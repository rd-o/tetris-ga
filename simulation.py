import multiprocessing
import random
from tetris_game import TetrisGame
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm

from draw_tetris import DrawTetris  

screen_width = 800
screen_height = 600
block_size = 30


#def run_simulation(tetris_instance, chromosome):
#    draw_tetris_instance = DrawTetris(screen_width, screen_height, block_size)
#    clock = draw_tetris_instance.clock()
#    fall_speed = 0.27
#    move_speed = 1
#    fall_time = 0
#    move_time = 0
#    run = True
#    while run:
#        # Here, use the chromosome's weights to decide on the best move
#        grid = tetris_instance.create_grid()
#
#        fall_time += clock.get_rawtime()
#        move_time += clock.get_rawtime()
#        clock.tick()
#
#        if fall_time / 1000 >= fall_speed:
#            fall_time = 0
#            run = tetris_instance.update_game_state()
#
#        if move_time / 1000 >= move_speed:
#            move_time = 0
#            move = chromosome.choose_move(tetris_instance, grid)  # Implement `choose_move` in chromosome
#            print(f"move: {move}")
#            tetris_instance.move(move)
#
#        #tetris_instance.update_game_state()
#
#        draw_tetris_instance.draw_grid(grid)
#        draw_tetris_instance.draw_current_piece(tetris_instance)
#        draw_tetris_instance.update()
        
        # Update the game state (e.g., move piece down, clear rows)

#    return tetris_instance.calculate_score()  # Return the score as the fitness

#def run_game_instance(chromosome):
#    # Create a TetrisGame instance for each chromosome
#    game_instance = TetrisGame(10, 20)
#    
#    # Run the simulation using the chromosome
#    score = run_simulation(game_instance, chromosome)
#    return score

# Example usage of TetrisGame in a multiprocessing setup
#def __init__(self, weight_lines_cleared, weight_height, weight_holes, weight_wells):
def create_chromosome():
    return Chromosome(random.uniform(-1, 1), 
                      random.uniform(-1, 1),
                      random.uniform(-1, 1),
                      random.uniform(-1, 1))

if __name__ == "__main__":
    #POPULATION_SIZE = 100
    #population = [Chromosome() for _ in range(POPULATION_SIZE)]
    #with multiprocessing.Pool() as pool:
    #    scores = pool.map(run_game_instance, population)
    #import pdb

    #pdb.set_trace()
    ##chromosome = Chromosome()
    ##run_game_instance(chromosome)
    #print("Scores for this generation:", scores)

    draw_tetris_instance = DrawTetris(screen_width, screen_height, block_size)
    ga = GeneticAlgorithm(population_size=50, mutation_rate=0.1, crossover_rate=0.7)
    ga.initialize_population(create_chromosome)

    # Run the evolution process
    for generation in range(10):
        print(f"Generation {generation}")
        ga.evaluate_fitness_1()
        best_chromosome = max(ga.population, key=lambda chromo: chromo.fitness)
        print(f"Best fitness: {best_chromosome.fitness}")
        ga.evolve()

