# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    """
    LOGIC:
    1.Start by putting the starting node on top of the stack
    2.Pop the top item of the stack and add it to the visited list of nodes
    3.Create a list of nodes that are adjacent to that popped node.
      Add the unvisited successor nodes to the stack
    4.Repeat steps 2 and 3 until the stack is empty
    """
    
    # The data structure we use for the fringe in DFS is a stack
    # Initialise a stack
    stack_dfs = util.Stack()
    
    # Get the initial state (start node) of the game problem using helper function
    initialState = problem.getStartState()

    # Check if the initial state is the final goal state; if yes return the list
    if problem.isGoalState(initialState):
        return []
    
    # Add the startNode along with the path so far (empty list) to the stack
    stack_dfs.push((initialState,[]))

    # List to store all the nodes that have already been visited
    visited_nodes = []

    # DFS LOOP
    while (stack_dfs.isEmpty() == False):
        # current node is of form (location, path)
        curr_node = stack_dfs.pop()

        # Check if current node is the desired goal state
        if problem.isGoalState(curr_node[0]):
            return curr_node[1] #path
        
        # Since we visit current node, we add it to visited nodes list
        visited_nodes.append(curr_node[0])

        # Store all the neighboring successor nodes of current node
        successor_nodes = problem.getSuccessors(curr_node[0])

        for node in successor_nodes:
            if node[0] in visited_nodes:
                # Don't do anything, as node has already been visited
                continue
            else:
                # Otherwise push the tuple (node, old path + node) onto the stack 
                new_path = curr_node[1] + [node[1]]
                stack_dfs.push((node[0],new_path))

    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    """
    LOGIC:
    1. We start by putting the starting node at the end of a queue
    2. Then take the front item of the queue and add it to the list of visited nodes
    3. Create a list of nodes that are adjacent to that popped node.
       Add the unvisited nodes to the back of the queue
    4. Repeat steps 2 and 3 until the queue is empty
    """
    "*** YOUR CODE HERE ***"
    # The data structure we use for the fringe in BFS is a queue
    # Initialise a Queue
    queue_bfs = util.Queue()

    # Get the initial state (start node) of the game problem using helper function
    initialState = problem.getStartState()

    # Check if the initial state is the final goal state; if yes return the list
    if problem.isGoalState(initialState):
        return []
    
    # Add the startNode along with the path so far (empty list) to the queue
    queue_bfs.push((initialState,[]))
    
    # List to store all the nodes that have already been visited
    visited_nodes = []

    # Since we are at the initial state, add it to the visited list
    visited_nodes.append(initialState)
    
    # BFS LOOP
    while (queue_bfs.isEmpty() == False):
        # current node is of form (location, path)
        curr_node = queue_bfs.pop()

        # Check if current node is the desired goal state
        if problem.isGoalState(curr_node[0]):
            return curr_node[1] #path

        # Store all the neighboring successor nodes of current node
        successor_nodes = problem.getSuccessors(curr_node[0])

        for node in successor_nodes:
            if node[0] in visited_nodes:
                # Don't do anything, as node has already been visited
                continue
            else:
                # Otherwise push the tuple (node, old path + node) onto the queue 
                new_path = curr_node[1] + [node[1]]
                queue_bfs.push((node[0],new_path))

                # Mark node as visited
                visited_nodes.append(node[0])

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """
    LOGIC: (Similar to BFS, except the costs)
    1.Start by putting the starting node into the PQ, along with cost associated (which is 0 initially)
    2.Pop the items of the PQ and add it to the visited list of nodes if it hasn't been visited
      Popped in order of priority (in our case cost is the basis for priority)
    3.Create a list of nodes that are adjacent to that popped node (neighboring nodes)
    4.For each adjacent node calculte new cost
    5.Repeat the steps until the PQ is empty
    """
    # The data structure we use for the fringe in UCS is a priority queue
    # Initialise a Priority Queue
    pq_ucs = util.PriorityQueue()

    # Get the initial state (start node) of the game problem using helper function
    initialState = problem.getStartState()

    # Check if the initial state is the final goal state; if yes return the list
    if problem.isGoalState(initialState):
        return []
    
    # Add the startNode along with the path so far (empty list), and cost to the pq
    pq_ucs.push((initialState,[], 0), 0)
    
    # List to store all the nodes that have already been visited
    visited_nodes = []

    # Though we are at the initial state, we don't add it to the visited list
    # This is bcz we generate successor nodes only if the curr node is not visited

    # UCS LOOP
    while (pq_ucs.isEmpty() == False):
        # current node is of form (location, path, cost)
        curr_node = pq_ucs.pop()

        # Check if current node is the desired goal state
        if problem.isGoalState(curr_node[0]):
            return curr_node[1] #path

        # Check if node is not visited, and only then add it to the visited_list
        # In order to avoid repeating nodes
        if curr_node[0] in visited_nodes:
            continue
        else:
            # Mark the node as visited
            visited_nodes.append(curr_node[0])
                
            # Store all the neighboring successor nodes of current node
            successor_nodes = problem.getSuccessors(curr_node[0])

            for node in successor_nodes:
                if node[0] in visited_nodes:
                    continue
                else:
                    # Calculate the new cost and the new path list, push it to the pq
                    new_cost = curr_node[2] + node[2]
                    new_path = curr_node[1] + [node[1]]
                    pq_ucs.push((node[0], new_path, new_cost), new_cost)


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """
    LOGIC: Same as UCS, instead of min cost Astar picks the node with minimum f(n) value
    f(n) = g(n) + h(n)
    Where g(n) = path cost from start node to current node (n)
          h(n) = path cost from current node (n) to the goal state
    """
    
    # The data structure we use for the fringe in A* is a priority queue
    # Initialise a Priority Queue
    pq_Astar = util.PriorityQueue()

    # Get the initial state (start node) of the game problem using helper function
    initialState = problem.getStartState()

    # Check if the initial state is the final goal state; if yes return the list
    if problem.isGoalState(initialState):
        return []
    
    # Add the startNode along with the path so far (empty list) to the pq
    pq_Astar.push((initialState,[], 0), 0)
    
    # List to store all the nodes that have already been visited
    visited_nodes = []

    # UCS LOOP
    while (pq_Astar.isEmpty() == False):
        # current node is of form (location, path, cost)
        curr_node = pq_Astar.pop()

        # Check if current node is the desired goal state
        if problem.isGoalState(curr_node[0]):
            return curr_node[1] #path

        # Check if node is not visited, and only then add it to the visited_list
        # In order to avoid repeating nodes
        if curr_node[0] in visited_nodes:
            continue
        else:
            # Mark the node as visited
            visited_nodes.append(curr_node[0])
                
            # Store all the neighboring successor nodes of current node
            successor_nodes = problem.getSuccessors(curr_node[0])

            for node in successor_nodes:
                if node[0] in visited_nodes:
                    continue
                else:
                    # Calculate the new cost and the new path list, push it to the pq
                    new_cost = curr_node[2] + node[2]
                    new_path = curr_node[1] + [node[1]]
                    
                    #f_n = h_n + g_n (cost from successor to goal + cost from start to current node)
                    g_n = new_cost
                    h_n = heuristic(node[0], problem)
                    f_n = g_n + h_n
                    pq_Astar.push((node[0], new_path, new_cost), f_n)
                
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
