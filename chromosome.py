#import random

class Chromosome:
#    def __init__(self):
#        self.weight_lines_cleared = random.uniform(-1, 1)
#        self.weight_height = random.uniform(-1, 1)
#        self.weight_holes = random.uniform(-1, 1)
#        self.weight_wells = random.uniform(-1, 1)
#
#    def __repr__(self):
#        return (f"Chromosome("
#                f"lines_cleared={self.weight_lines_cleared:.2f}, "
#                f"height={self.weight_height:.2f}, "
#                f"holes={self.weight_holes:.2f}, "
#                f"wells={self.weight_wells:.2f})")

    def __init__(self, weight_lines_cleared, weight_height, weight_holes, weight_wells):
        self.weight_lines_cleared = weight_lines_cleared
        self.weight_height = weight_height
        self.weight_holes = weight_holes
        self.weight_wells = weight_wells

    def evaluate_state(self, game_state):
        """
        Evaluate the score of a game state using the chromosome's weights.
        :param game_state: A dictionary containing features like:
                           {'lines_cleared': int, 'height': int, 'holes': int, 'wells': int}
        :return: A weighted score for the game state.
        """
        return (
            self.weight_lines_cleared * game_state['lines_cleared'] +
            self.weight_height * game_state['height'] +
            self.weight_holes * game_state['holes'] +
            self.weight_wells * game_state['wells']
        )

    def choose_move(self, tetris_instance, grid):
        """
        Analyze possible moves in the game and choose the best one.
        :param tetris_instance: An instance of the Tetris game containing the current grid
                                and available moves.
        :return: The best move as a string ('left', 'right', 'rotate', 'drop').
        """
        best_move = None
        best_score = float('-inf')  # Start with a very low score

        possible_moves = tetris_instance.get_possible_moves()  # Retrieve all valid moves
        for move in possible_moves:
            # Simulate the move on a copy of the game state
            simulated_state = tetris_instance.simulate_move(move, grid)
            
            # Evaluate the simulated game state
            score = self.evaluate_state(simulated_state)
            print(f"simulated score: {score} for move: {move}")

            # If this move results in a better score, update the best move
            if score > best_score:
                best_score = score
                best_move = move

        return best_move



