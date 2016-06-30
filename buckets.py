"""
buckets.py

Bucket game in Python (2/3).

How to play?
>>> from buckets import *
>>> m = Manager()
>>> p = BucketPlayer(m)
>>> p.playGame(3, 5, 4)  # Bucket A=3L, B=5L, Want=4L
Solution is
[0, 0]
[0, 5]
[3, 2]
[0, 2]
[2, 0]
[2, 5]
[3, 4]
>>>
"""


class Manager:
    """
    Manage game queue. Keep track of states already seen
    and who their parent states are.
    """

    def __init__(self):
        self.queue = []
        self.seen = {}

    def getState(self):
        """
        Return next state and pop it off the queue.
        """
        # TODO: return a state from the queue if it exists
        pass

    def addState(self, parentState, newState):
        """
        Add state if it's new. Remember its parent
        """
        # TODO: add a state to the queue and seen states
        pass

    def getSolution(self):
        """
        Return solution from latest state added.
        """
        # TODO: return all states required for the solution
        pass

    def getParent(self, childState):
        """
        Return parent of state, if it exists.
        """
        # TODO: return parent if it exists
        pass

class BucketPlayer:
    def __init__(self, manager):
        self.manager = manager

    def test(self, oldstate, newstate):
        # TODO: implement
        pass

    def playGame(self, aMax, bMax, goal):
        """
        Grab a state and generate 8 more to submit to the manager.
        """
        self.goal = goal
        self.manager.addState("", [0, 0])   # start with 2 empty buckets

        while 1:
            # TODO: player actions
            break

        print ("Solution is ")
        print ("\n".join(self.manager.getSolution()))
