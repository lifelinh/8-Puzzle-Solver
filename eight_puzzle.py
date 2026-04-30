#
# eight_puzzle.py (Final Project)
#
# driver/test code for state-space search on Eight Puzzles
#

from searcher import *

def create_searcher(algorithm, depth_limit = -1, heuristic = None):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
            
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(depth_limit)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(depth_limit)
    elif algorithm == 'DFS':
        searcher = DFSearcher(depth_limit)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(depth_limit, heuristic)
    elif algorithm == 'A*':
        searcher = AStarSearcher(depth_limit, heuristic)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, depth_limit = -1, heuristic = None):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
    """
    
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, depth_limit, heuristic)
    if searcher == None:
        return

    soln = None
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, depth_limit = -1, heuristic = None):
    """ Function that will solve all of the 8-Puzzles with algorithm in
    filename, with an optional depth_limit, default as -1, and heuristic,
    default as None
    input filename: str of a filename containing digit strings representing a
    puzzle for each line
    input algorithm: str of a defined algorithm name in Searcher class
    input depth_limit: int > 0
    input heuristic: heuristic function
    """
    
    # Accumulator variables for the amount solved, with the total moves and
    # states tested with every iteration over lines in filename
    solved = 0
    moves = 0
    states = 0
    
    # Open the file so that the loop can iterate over the lines
    file = open(filename, 'r')
    for digitstr in file:
        # Modeled after the eight_puzzle function and written with guidelines
        # from instructions of the project
        digitstr = digitstr.strip()
        init_board = Board(digitstr)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, depth_limit, heuristic)
        soln = None
        
        try:
            soln = searcher.find_solution(init_state)
            
        except KeyboardInterrupt:
            print('search terminated, ', end='')
            
        if soln == None:
            print(f'{digitstr}: no solution')
            
        # Accumulate the solved, moves, and states variables which are going to
        # be used to calculate the average number of moves and states, with
        # the total number of puzzles solved. Only accumulate if the puzzle
        # was solved, or else the averages will be inaccurate.
        else:
            print(f'{digitstr}: {soln.num_moves} moves, {searcher.num_tested} states tested')
            solved += 1
            moves += soln.num_moves
            states += searcher.num_tested
            
    # Print a blank line and the amount of solved puzzles
    print()
    print(f'solved {solved} puzzles')
    
    # Print averages if there were puzzles solved
    if solved != 0:
        # Calculate the average moves and states per solved puzzle, which will 
        # be printed with the output
        avg_moves = moves/solved
        avg_states = states/solved
        print(f'averages: {avg_moves} moves, {avg_states} states tested')