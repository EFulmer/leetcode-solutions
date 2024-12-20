# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(left=root.left, right=root.right, level=0)
        return root

    def helper(
        self,
        left: Optional[TreeNode]=None,
        right: Optional[TreeNode]=None,
        level: Optional[int]=0
    ):
        # assuming a perfect tree
        if not left:
            return
        # if even, swap children, doing bitwise tricks for an efficiency gain
        if (level & 1) == 0:
            left.val, right.val = right.val, left.val
        # two recursive calls
        # one for the "outer" and and one for the "inner" subtree
        # to preserve the structure
        self.helper(left=left.left, right=right.right, level=level+1)
        self.helper(left=left.right, right=right.left, level=level+1)
