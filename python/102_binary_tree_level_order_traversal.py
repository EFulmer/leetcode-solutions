# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Keep two stacks: one for the values and one for the
        # next nodes to traverse.
        # For each level:
        # Create a new level to the traversal values stack and push
        # all the nodes onto it.
        # Push the children onto the next nodes stack.
        if root is None:
            return []
        result = []
        to_traverse = [root]
        while len(to_traverse) > 0:
            new_layer = [node.val for node in to_traverse]
            result.append(new_layer)
            new_traverse = []
            for node in to_traverse:
                if node.left is not None:
                    new_traverse.append(node.left)
                if node.right is not None:
                    new_traverse.append(node.right)
            to_traverse = new_traverse
        return result
