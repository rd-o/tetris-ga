from chromosome import Chromosome
from tetris_game import TetrisGame
import random

# Screen dimensions
screen_width = 300
screen_height = 600
block_size = 30

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = []  # List of Chromosome objects

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

    def evaluate_fitness(self):
        """Evaluate the fitness of each chromosome in the population."""
        for chromosome in self.population:
            total_score = 0
            for _ in range(3):  # Play 3 games to average the performance
                tetris_game = TetrisGame(screen_width // block_size, screen_height // block_size)
                tetris_game.setup_pygame()
                score = self.play_game(chromosome, tetris_game)
                total_score += score
            chromosome.fitness = total_score / 3

    def play_game(self, chromosome, tetris_game):
        """Simulate a game of Tetris using the chromosome's strategy."""
        run = True
        while run:
            run = tetris_game.update_with_graphics()
            tetris_game.check_movement(chromosome)

        score = tetris_game.score
        print(f"score: {score}")
        return score



