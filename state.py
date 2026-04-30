#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#

from board import *

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    
    ### Add your method definitions here. ###
    def __init__(self, board, predecessor, move):
        """ constructor for the State object, which stores the Board object
        associated with the state, the predecessor state, the move that was
        done to get to the state from the predecessor, and the number of moves
        done from the initial state to the current state
        """
        
        self.board = board
        self.predecessor = predecessor
        self.move = move
        
        # There are no moves yet if the state is the initial state
        if predecessor == None:
            self.num_moves = 0
            
        # If there is a predecessor with moves, the number of moves of this
        # state will be 1 higher than the predecessor's.
        else:
            self.num_moves = predecessor.num_moves + 1
    
    def is_goal(self):
        """ Return a Boolean value depending if the input state is the goal
        """
        
        # Check if the 2D list represented by self.board.tiles is the same as
        # GOAL_TILES's 2D list
        return self.board.tiles == GOAL_TILES
    
    def generate_successors(self):
        """ Create copies of the Board object, and apply different moves to
        each copy, generating successor State objects if the move was possible
        """
        
        # Start with an empty list
        successors = []
        
        # Iterate over all the possible moves, and apply them to a copy of the
        # board so the original state isn't changed
        for m in MOVES:
            b = self.board.copy()
            
            # If it is possible to apply the move, add it to the list 
            if b.move_blank(m):
                successors += [State(b, self, m)]
                
        return successors
    
    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        
        # You should *NOT* change this method.
        return True

    def print_moves_to(self):
        """ Follows the state search tree, printing every step from the initial
        state to the object the method is called on
        """
        
        # When there is no predecessor, it means it is the initial state, so
        # print it's board and identify it as the initial state.
        if not self.predecessor:
            print('initial state:')
            print(self.board)
            
        # If there is not a base case, then call the method recursively on the
        # predecessor, and print the move as well as the board that results
        # from the move.
        else:
            self.predecessor.print_moves_to()
            print(f'move the blank {self.move}')
            print(self.board)