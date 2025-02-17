# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # let's start by asserting that p is always < q
        # (all nodes have unique values so no need for <=)
        if p.val > q.val:
            p, q = q, p

        # If either node is somehow null, then just return the root.
        if p is None:
            return root
        if q is None:
            return root

        # Otherwise, we rely on the fact that this is a binary search
        # tree.
        # If p < root < q, then we've found the LCA, since either
        # subtree (left or right) will have only one of p or q.
        # Why? Because either subtree will only have one of p or q.
        # Since q > root, then the LCA can't be in the left subtree
        # since q isn't in that subtree. Same for p, just flip the
        # signs.
        if p.val < root.val < q.val:
            return root
        # If one of the nodes has the same value as the root (or
        # current node, since we're recursing), we've found the answer,
        # since we're guaranteed each node is unique
        elif p.val == root.val or q.val == root.val:
            return root
        # Otherwise, if root < p < q, then the LCA must be in the right
        # subtree since its value is > the root's.
        elif root.val < p.val < q.val:
            return self.lowestCommonAncestor(root=root.right, p=p, q=q)
        # The final case is if p < q < root, so flipped from the last
        # one, and we recurse into the left subteee.
        else:
            return self.lowestCommonAncestor(root=root.left, p=p, q=q)
