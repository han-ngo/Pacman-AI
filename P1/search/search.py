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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    curState = problem.getStartState()

    visited = []
    stack = util.Stack()  # STACK - LIFO
    stack.push((curState, []))  # state, [actions]

    # while stack is not empty
    while not stack.isEmpty():
        # pop stack and check all non-visited successors for goal
        curState, actions = stack.pop()
        visited.append(curState)  # mark as visited

        if problem.isGoalState(curState):
            return actions

        # checking all successors
        successors = problem.getSuccessors(curState)
        for successorState, directions, cost in successors:
            if successorState not in visited:
                stack.push((successorState, actions + [directions]))

    return actions


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    cur = problem.getStartState()

    visited = [cur]
    q = util.Queue()  # QUEUE - FIFO
    q.push((cur, []))  # state, [actions]

    while not q.isEmpty():
        # pop queue and check for goal
        curState, actions = q.pop()

        if problem.isGoalState(curState):
            return actions

        # checking all successors
        successors = problem.getSuccessors(curState)
        for successorState, directions, cost in successors:
            # pushing successors to queue if not visited
            if successorState not in visited:
                visited.append(successorState)  # mark as visited
                q.push((successorState, actions + [directions]))

    return actions


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    cur = problem.getStartState()

    visited = []
    q = util.PriorityQueue()  # PRIORITY QUEUE - FIFO
    q.push((cur, [], 0), 0)  # (state, [actions], cost), priority
    while not q.isEmpty():
        # pop queue with lowest cost
        curState, actions, cost = q.pop()
        if curState not in visited:
            visited.append(curState)
            if problem.isGoalState(curState):
                return actions
            for (
                successorState,
                successorActions,
                successorCost,
            ) in problem.getSuccessors(curState):
                q.push(
                    (
                        successorState,
                        actions + [successorActions],
                        cost + successorCost,
                    ),
                    cost + successorCost,
                )
    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    cur = problem.getStartState()

    q = util.PriorityQueue()
    q.push((cur, [], 0), heuristic(cur, problem))
    visited = []
    while q:
        state, actions, cost = q.pop()
        if state not in visited:
            visited.append(state)
            if problem.isGoalState(state):
                return actions
            for next_state, next_action, next_cost in problem.getSuccessors(state):
                q.push(
                    (next_state, actions + [next_action], cost + next_cost),
                    cost + next_cost + heuristic(next_state, problem),
                )
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
