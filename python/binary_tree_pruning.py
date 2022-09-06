# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # for each node:
        # if the node's value is 0, then mark it for deletion
        # do a logical AND with marked_for_deletion and should_left_subnode_be_deleted and should_right_subnode_be_deleted?
        # if ^^^ is true:
        # nuke em
        # if not:
        # go on to the left and right subtrees that remain
        # ...
        # the problem is, how do you delete yourself?
        # check if left and right should be pruned
        # act on those, and then traverse what's left
        prune_left = self.should_tree_be_pruned(root.left)
        prune_right = self.should_tree_be_pruned(root.right)
        if prune_left:
            root.left = None
        else:
            root.left = self.pruneTree(root.left)
        if prune_right:
            root.right = None
        else:
            root.right = self.pruneTree(root.right)
        # finally, what if you end up with a singleton?
        if root.val == 0 and not (root.left or root.right):
            return None
        return root

    def should_tree_be_pruned(self, root):
        if not root:
            return True  # default true because we use And, and deleting an empty tree is fine
        marked_for_deletion = (root.val == 0) and (self.should_tree_be_pruned(root.left)) and (self.should_tree_be_pruned(root.right))
        return marked_for_deletion
