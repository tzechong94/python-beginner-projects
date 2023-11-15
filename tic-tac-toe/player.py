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