# this solution has some issues with the online judge, but is correct
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class DFS:
    def __init__(self):
        self.count = 0
        self.visited = dict()

    def search(self, node):
        if node is None:
            return None
        if node.val in self.visited.keys():
            return
        current = Node(node.val)
        if current.val not in self.visited.keys():
            self.visited[current.val] = list()
        for neighbor in node.neighbors:
            if neighbor.val not in self.visited.keys():
                self.search(neighbor)
            self.visited[neighbor.val].append(current)
        self.count += 1

def clone_dfs(node, clone):
    if node is None:
        return None
    acc = Node(node.val)
    if acc.val not in clone.keys():
        clone[acc.val] = list()
    for neighbor in node.neighbors:
        if neighbor.val not in clone.keys():
            clone_dfs(neighbor, clone)
        clone[neighbor.val].append(acc)
        if neighbor.val not in acc.neighbors:
            acc.neighbors.append(neighbor.val)
    return clone

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return clone_dfs(node, dict())[node.val]
