# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return check_height_balance(root) is not None


def check_height_balance(root: Optional[TreeNode]) -> Optional[int]:
    # Height balance:
    # Height difference between the left and right subtrees is max 1,
    # and each subtree is also height-balanced.
    # We terminate early by returning None if we see the conditions
    # are not satisfiable in the middle of processing some subtree.
    #
    # Check the base case first:
    if root is None:
        return 0

    # Check the subtrees:
    left_height = check_height_balance(root.left)
    if left_height is None:
        return None

    right_height = check_height_balance(root.right)
    if right_height is None:
        return None

    # Check that their height difference is at most one:
    height_diff = abs(left_height - right_height)
    if height_diff > 1:
        return None

    # And finally, we take the greater S.T. height for use in
    # comparisons that get made in earlier calls of this function,
    # this is to ensure we don't miss some height-unbalanced subtrees.
    # Stricter = better here!
    return_height = max(left_height, right_height)
    return 1 + return_height
