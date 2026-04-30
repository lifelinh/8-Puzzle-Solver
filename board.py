#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        # Iterate over every slot in the grid, updating the values according
        # to the position in digitstr, and the row and column of the blank
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = int(digitstr[3 * r + c])
                if self.tiles[r][c] == 0:
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###
    def __repr__(self):
        """ Overwrite print statements when called on Board objects, returning
        a 3 by 3 grid arranged with the numeric tiles and the blank.
        """
        
        # Start with an empty string
        s = ''
        
        # Iterate over every slot in the grid
        for r in range(3):
            for c in range(3):
                
                # Create the underscore if the tile is 0
                if self.tiles[r][c] == 0:
                    s += '_ '
                    
                # Update s with the appropriate value according to the index
                else:
                    s += f'{self.tiles[r][c]} '
                    
            # Go to the next line when a row has been iterated over
            s += '\n'
            
        return s
    
    def move_blank(self, direction):
        """ Moves the blank slot in direction, and also returns a Boolean value
        if the movement was possible or not.
        """
        
        # Store the new row and column of the blank in variables
        if direction == 'up':
            new_r = self.blank_r - 1
            new_c = self.blank_c
        elif direction == 'down':
            new_r = self.blank_r + 1
            new_c = self.blank_c
        elif direction == 'left':
            new_r = self.blank_r
            new_c = self.blank_c - 1
        elif direction == 'right':
            new_r = self.blank_r
            new_c = self.blank_c + 1
            
        # If the input was not one of the four, it was not a valid direction
        else:
            print(f'unknown direction: {direction}')
            return False
        
        # Check if the movement results in the blank being out of bounds
        if new_r not in [0, 1, 2] or new_c not in [0, 1, 2]:
            return False
        
        # Update values of the tiles that are being moved, swapping them, and
        # also updating the values of blank_r and blank_c
        else:
            self.tiles[self.blank_r][self.blank_c] = self.tiles[new_r][new_c]
            self.tiles[new_r][new_c] = 0
            self.blank_r = new_r
            self.blank_c = new_c
            return True
    
    def digit_string(self):
        """ Returns a digitstring that represents all numeric tiles in order
        """
        
        # Create an empty string to concatenate string numbers to it 
        digitstr = ''
        
        # Iterate over all tiles in order and concatenate the number, which is
        # converted to a string, to digitstr
        for r in range(3):
            for c in range(3):
                digitstr += str(self.tiles[r][c])
                
        return digitstr
    
    def copy(self):
        """ Return a deep copy of the board
        """
        
        # Construct a new board using the digit_string method and return it
        return Board(self.digit_string())
    
    def num_misplaced(self):
        """ Returns how many tiles are not in the correct place
        """
        
        wrong = 0
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != goal[r][c] and self.tiles[r][c] != 0:
                    wrong += 1
        return wrong
    
    def __eq__(self, other):
        """ Overwrite the == operator to check if both Board objects have the
        same values, regardless of memory ID
        """
        
        # Compare the 2D list represented by self.tiles and other.tiles
        return self.tiles == other.tiles