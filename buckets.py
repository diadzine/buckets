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
        if not self.queue:
            return None

        state = self.queue[0]
        self.queue = self.queue[1:]
        return state

    def addState(self, parentState, newState):
        """
        Add state if it's new. Remember its parent
        """
        if str(newState) in self.seen:
            return

        self.seen[str(newState)] = str(parentState)
        self.queue.append(newState)

    def getSolution(self):
        """
        Return solution from latest state added.
        """
        solution = []
        state = self.queue[-1]

        while state:
            solution.append(str(state))
            state = self.getParent(state)

        solution.reverse()
        return solution

    def getParent(self, childState):
        """
        Return parent of state, if it exists.
        """
        try:
            return self.seen[str(childState)]
        except:
            return None


class BucketPlayer:
    def __init__(self, manager):
        self.manager = manager

    def test(self, oldstate, newstate):
        [newA, newB] = newstate
        won = (newA == self.goal or newB == self.goal)
        self.manager.addState(oldstate, newstate)
        return won

    def playGame(self, aMax, bMax, goal):
        """
        Grab a state and generate 8 more to submit to the manager.
        """
        self.goal = goal
        self.manager.addState("", [0, 0])   # start with 2 empty buckets

        while 1:
            oldstate = self.manager.getState()
            [aHas, bHas] = oldstate

            if self.test(oldstate, [aMax, bHas]):
                break  # fill A from well

            if self.test(oldstate, [0, bHas]):
                break  # empty A to well

            if self.test(oldstate, [aHas, bMax]):
                break  # fill B from well

            if self.test(oldstate, [aHas, 0]):
                break  # empty B to well

            howmuch = min(aHas, bMax-bHas)

            if self.test(oldstate, [aHas-howmuch, bHas+howmuch]):
                break  # pour A to B

            howmuch = min(bHas, aMax-aHas)

            if self.test(oldstate, [aHas+howmuch, bHas-howmuch]):
                break  # pour B to A

        print ("Solution is ")
        print ("\n".join(self.manager.getSolution()))
