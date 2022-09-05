"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        nodes_by_level = {}
        self.helper(root, nodes_by_level, 0)
        result = []
        for level in sorted(nodes_by_level.keys()):
            result.append(nodes_by_level[level])
        return result

    def helper(self, current_node, node_level_mapping, current_level):
        if not current_node:
            return
        current_level_nodes = node_level_mapping.get(current_level, [])
        current_level_nodes.append(current_node.val)
        node_level_mapping[current_level] = current_level_nodes
        for child in current_node.children:
            self.helper(child, node_level_mapping, current_level+1)
