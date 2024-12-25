# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode]) -> dict[str, int]:
        if not root:
            return dict(height=0, diameter=0)

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        current_height = 1 + max(left["height"], right["height"])
        current_diameter = left["height"] + right["height"]
        max_diameter = max(current_diameter, left["diameter"], right["diameter"])

        return dict(height=current_height, diameter=max_diameter)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stats = self.dfs(root)
        return stats["diameter"]
