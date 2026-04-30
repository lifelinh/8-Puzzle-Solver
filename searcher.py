#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """ Constructor for the object, which stores the untested states, the 
        number of states tested, and the maximum depth the searcher will go
        """
        
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def should_add(self, state):
        """ Returns a Boolean value based on whether if a state should be
        added to the object's list of untested states, depending if it is
        within or beyond the depth limit or can create a searching loop
        """
        
        # If the state causes a cycle, it should not be added
        if state.creates_cycle():
            return False
        
        # If the number of moves required to get to a state is greater than
        # the depth limit, it is beyond the depth limit and shouldn't be added
        elif self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False

        else:
            return True
         
    def add_state(self, new_state):
        """ Adds a new state to the searcher's list of untested states
        """
        self.states.append(new_state)
            
    def add_states(self, new_states):
        """ Adds states that should be added to the list of untested states
        from new_states
        """
        
        # Iterate over every state in the list, only adding it to the list of
        # untested states if it should be added
        for s in new_states:
            if self.should_add(s):
                self.add_state(s)
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        
        s = random.choice(self.states)
        self.states.remove(s)
        return s
            
    def find_solution(self, init_state):
        """ Continues to test and search through states until the solution is
        found or when there are no more states to test, returning None if so
        """
        
        self.add_state(init_state)
        while self.states:
            
            # Track the amount of tests, necessary for staying in depth limit
            self.num_tested += 1
            
            # Pick a state to test next
            testing_state = self.next_state()
            
            # Return the tested state if it is the goal, which ends the loop
            if testing_state.is_goal():
                return testing_state
            
            # Generate and add successors to the list and repeat the loop
            else:
                successors = testing_state.generate_successors()
                self.add_states(successors)
        
        # If the loop ends and nothing has been returned, it means the list of
        # states remaining to be tested is empty, so there is no solution
        return None
    
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ Searcher class object that will search breadth-first by picking states 
    to search with the smallest depth in order
    """
    
    def next_state(self):
        """ Overwrite the next_state method of the superclass with a
        specialization that picks the state that has been in the list of
        untested states the longest
        """
        
        # Index 0 is the one that has been in the list the longest, as states
        # are appended to the end of the list with the add_states method
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    """ Searcher class object that will search with a depth-first approach by
    always choosing the state with the deepest depth
    """
    
    def next_state(self):
        """ Overwrite the method of the superclass with specialization that
        picks the state that is the newest in the list of untested states
        """
        
        # Index -1 is the one that has most recently been added to the list,
        # as the add_states method appends generated successors to the end
        s = self.states[-1]
        self.states.remove(s)
        return s
    
def h0(state):
    """ a heuristic function that always returns 0 """
    
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ A heuristic function for use in the GreedySearcher and AStarSearcher
    objects, which will return the number of misplaced tiles
    """
    return state.board.num_misplaced()

def h2(state):
    """ A better heuristic function for use in the GreedySearcher and
    AStarSearcher objects, which returns how far misplaced tiles are from their
    goal position, with taxicab distance
    """
    
    # Total distance of all the tiles, which will be accumulated for every
    # misplaced tile.
    h = 0
    goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    
    for r in range(3):
        for c in range(3):
            if state.board.tiles[r][c] != goal[r][c] and state.board.tiles[r][c] != 0:
                # A modulo of 0 indicates the tile is 0, 1, or 2 and should be
                # in row 0. For 1, it is 3, 4, or 5, and should be in row 1
                # For 2, it is 6, 7, or 8 and should be in row 3. A similar
                # calculation works for the columns.
                goal_r = state.board.tiles[r][c] // 3
                goal_c = state.board.tiles[r][c] % 3
                
                # Calculate the absolute value of the distance, and add it to h.
                h += abs(r - goal_r) + abs(c - goal_c)
                
    return h
                
class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, depth_limit, heuristic):
        """ constructor for a GreedySearcher object
            inputs:
             * depth_limit - the depth limit of the searcher
             * heuristic - a reference to the function that should be used 
            when computing the priority of a state
        """
        
        # add code that calls the superclass constructor
        super().__init__(depth_limit)
        self.heuristic = heuristic
        
    def priority(self, state):
        """ Computes and returns the priority value of state, which is used by
        the searcher for picking what state to search through next
        """
        
        # Call a method to get the number of misplaced tiles on the board of
        # state, and multiply it by -1 so it can be used with the max operator
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """ Overwrite the method from the superclass with a specialization
        that will add a list of lists where the elements are the priority 
        paired with the state
        """
        
        self.states.append([self.priority(state), state])
        
    def next_state(self):
        """ Override the superclass method which will choose the next state to
        search based on it's priority value
        """
        
        # Get the list with the highest priority value, remove it, and return
        # only the state, which is index -1 of the list.
        s = max(self.states)
        self.states.remove(s)
        return s[-1]
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ A class for objects that perform AStar search algorithms on an 8 Puzzle
    """
        
    def priority(self, state):
        """ Compute and return the priority value of state, based on it's move
        cost so far and it's heuristic value based on the misplaced tiles
        """
        
        # Adds the number of oves so far to the heuristic value before 
        # multiplying it by -1
        return -1 * (self.heuristic(state) + state.num_moves)
    
    def add_state(self, state):
        """ Override the method from GreedySearcher to use the specialized
        version of the priority method rather than GreedySearcher's priority
        """
        
        self.states.append([self.priority(state), state])