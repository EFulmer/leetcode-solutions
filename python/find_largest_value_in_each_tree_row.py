# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def recurse(self, node: Optional[TreeNode], map: Dict, level: int):
        if not node:
            return

        if node.left is not None:
            map[level].append(node.left.val)
        if node.right is not None:
            map[level].append(node.right.val)

        self.recurse(node=node.left, map=map, level=level+1)
        self.recurse(node=node.right, map=map, level=level+1)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        row_numbers_to_values = defaultdict(list)
        if root.val is not None:  # in case the value is 0
            row_numbers_to_values[0].append(root.val)
        self.recurse(node=root, level=1, map=row_numbers_to_values)
        result = []
        for k, v in row_numbers_to_values.items():
            result.append(max(v))
        return result
