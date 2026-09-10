from collections import deque

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.states = set()

    def add(self, node):
        self.frontier.append(node)
        self.states.add(node.state)

    def contains_state(self, state):
        return state in self.states

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier.pop()
        self.states.discard(node.state)
        return node


class QueueFrontier(StackFrontier):
    def __init__(self):
        super().__init__()
        self.frontier = deque()
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier.popleft()
        self.states.discard(node.state)
        return node
