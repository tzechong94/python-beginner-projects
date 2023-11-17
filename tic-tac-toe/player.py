import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8)')
            # we are going to check that this is a correct value by trying to cast it
            # to an integer, and if it's not then we stay it's invalid.
            # if that spot is not available on the board, we also say it's invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                value_square = True
            except ValueError:
                print('Invalid square, try again.')
            return val
        
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())

        else:
            # get square based off the minimax algo
            square = self.minimax(game, self.letter)
            
        return square
    
    def minimax(self, state, player):
        max_player = self.letter 
        other_player = 'O' if player == 'X' else 'X'

        # first, we want to check if the previous move is a winner
        # this is our base case
        if state.current_winner == other_player:
            #we should return position and score because we need to keep track of the score
            # for minimax to work
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1
                    )}
        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximise
        else: 
            best = {'position':None, 'score': math.inf} #each score should minimize

        for possible_move in state.available_moves():
            # step 1: Make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # now we alternate players
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # step 4: update the dictionaries if necessary 

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best

        return best