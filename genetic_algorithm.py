from multiprocessing import Pool
from chromosome import Chromosome
from tetris_game import TetrisGame
from draw_tetris import DrawTetris  
import random

#import tetris_game

# Screen dimensions
#screen_width = 300
screen_width = 900
screen_height = 600
block_size = 10


tetris_width = 10
tetris_height = 20

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = []  # List of Chromosome objects
        self.draw_tetris_instance = DrawTetris(screen_width, screen_height, block_size)
        self.counter = 0

    def initialize_population(self, create_chromosome):
        """Initialize the population with randomly generated chromosomes."""
        self.population = [create_chromosome() for _ in range(self.population_size)]

    def select_parents(self):
        """Select two parents using a selection method like tournament selection."""
        def tournament_selection():
            tournament_size = 3
            selected = random.sample(self.population, tournament_size)
            return max(selected, key=lambda chromo: chromo.fitness)

        return tournament_selection(), tournament_selection()

    def crossover(self, parent1, parent2):
        """Perform crossover to create a new child."""
        if random.random() < self.crossover_rate:
            child = Chromosome(
                weight_lines_cleared=(parent1.weight_lines_cleared + parent2.weight_lines_cleared) / 2,
                weight_height=(parent1.weight_height + parent2.weight_height) / 2,
                weight_holes=(parent1.weight_holes + parent2.weight_holes) / 2,
                weight_wells=(parent1.weight_wells + parent2.weight_wells) / 2,
            )
        else:
            child = random.choice([parent1, parent2])  # No crossover, clone one parent
        return child

    def mutate(self, chromosome):
        """Mutate a chromosome by slightly altering its weights."""
        if random.random() < self.mutation_rate:
            chromosome.weight_lines_cleared += random.uniform(-0.1, 0.1)
            chromosome.weight_height += random.uniform(-0.1, 0.1)
            chromosome.weight_holes += random.uniform(-0.1, 0.1)
            chromosome.weight_wells += random.uniform(-0.1, 0.1)

    def evolve(self):
        """Create the next generation by selecting parents, performing crossover, and mutating."""
        new_population = []
        for _ in range(self.population_size // 2):  # Create population_size/2 offspring pairs
            parent1, parent2 = self.select_parents()
            child1 = self.crossover(parent1, parent2)
            child2 = self.crossover(parent1, parent2)

            self.mutate(child1)
            self.mutate(child2)

            new_population.extend([child1, child2])

        self.population = new_population


    def play_game(self, chromosome, tetris_game):
        """Simulate a game of Tetris using the chromosome's strategy."""
        run = True
        while run:
            run = tetris_game.update_with_multiple_graphics()
            tetris_game.check_movement(chromosome)

        score = tetris_game.score
        print(f"score: {score}")
        return score

#    @staticmethod
#    def simulate_single_game(args):
#        """Simulate a single game for a given chromosome."""
#        chromosome, _ = args
#        tetris_game = TetrisGame(tetris_width, tetris_height)
#        tetris_game.setup_instance(self.draw_tetris_instance, self.counter)
#        self.counter += 1
#        return self.play_game(chromosome, tetris_game)
#
#    def evaluate_fitness(self):
#        """Evaluate fitness in batches, running 24 tasks concurrently (8 chromosomes x 3 games)."""
#        
#        # Prepare all tasks (each chromosome runs 3 games)
#        tasks = []
#        for chromosome in self.population:
#            tasks.extend([(chromosome, i) for i in range(3)])  # 3 games per chromosome
#
#        # Process tasks in batches of 24
#        batch_size = 1
#        for i in range(0, len(tasks), batch_size):
#            batch = tasks[i:i + batch_size]
#
#            with Pool() as pool:
#                results = pool.map(simulate_single_game, batch)
#
#            # Update fitness for each chromosome in the batch
#            for idx, chromosome in enumerate(self.population):
#                # Get the 3 scores for this chromosome
#                scores = results[idx * 3:(idx + 1) * 3]
#                chromosome.fitness = sum(scores) / len(scores)

    def evaluate_fitness_1(self):
        """Evaluate the fitness of each chromosome in the population."""
        for chromosome in self.population:
            chromosome.fitness = self.play_game_1(chromosome)

    def play_game_1(self, chromosome):
        """Simulate a game of Tetris using the chromosome's strategy."""
        tetris_game = []
        for i in range(3):
            tetris_game.append(TetrisGame(tetris_width, tetris_height))
            tetris_game[i].setup_instance(self.draw_tetris_instance, i)

        run = [True, True, True]
        while run[0] or run[1] or run[2]:
            for i in range(3):
                if run[i]:
                    run[i] = tetris_game[i].update_with_multiple_graphics()
                    tetris_game[i].check_movement(chromosome)

        total_score = 0
        for i in range(3):
            total_score += tetris_game[i].score
        
        score = total_score / 3
        print(f"score: {score}")
        return score
