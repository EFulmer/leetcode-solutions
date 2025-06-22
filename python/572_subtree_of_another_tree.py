# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # I will break this up into two cases:
        # First, we need to find the root of the subtree present in the
        # main tree.
        # Once we do that, we test for tree equality.
        # I'll do tree equality in a separate function.
        if root is None:
            return False
        elif root.val == subRoot.val:
            # If the roots match, there are two sub-cases:
            # 1. There is a subtree starting at the current node.
            # 2. There is an inequality between the two trees
            #    somewhere deeper down, so this is not a match,
            #    BUT there MAY be a match deeper in the tree.
            if trees_equal(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def trees_equal(tree_1: Optional[TreeNode], tree_2: Optional[TreeNode]) -> bool:
    if tree_1 is None and tree_2 is None:
        return True
    elif tree_1 is None and tree_2 is not None:
        return False
    elif tree_1 is not None and tree_2 is None:
        return False
    elif tree_1.val != tree_2.val:
        return False
    else:  # default case: trees have the same value at the root
        return trees_equal(tree_1.left, tree_2.left) and trees_equal(tree_1.right, tree_2.right)
