# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        queue = [root]
        while queue:
            current = queue.pop()
            if current.right:
                queue.append(current.left)
                queue.append(current.right)
                result += 2
            elif current.left:
                queue.append(current.left)
                result += 1
        return result + 1
