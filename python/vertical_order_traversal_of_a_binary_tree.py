# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # First, build a dict mapping each node's "coordinates" to its
        # value.
        # Since the problem definition states that multiple nodes can
        # have the same coordinates, we need to use a list to store
        # every node value at its coordinates.
        # We can easily do this with defaultdict.
        # the first set of keys are the columns, and the keys of the
        # inner dicts are the rows.
        order_mapping = defaultdict(lambda: defaultdict(list))
        self.helper(root, 0, 0, order_mapping)
        # Now, to create the result, we need to go column by column,
        # leftmost (lowest) to highest (greatest)
        result = []
        sorted_keys = sorted(order_mapping.keys())
        for column in sorted_keys:
            # The result is a singly-nested list, where the first item
            # of the outer list is everything in the leftmost column,
            # and the items of those list are the elements of that row,
            # from bottom to top.
            # Create a temporary list to build the current inner list
            # (for the current column).
            tr = []
            # In each column, we need to go by row by row, top (lowest)
            # to highest (greatest)
            for row in sorted(order_mapping[column]):
                # In the case of one coordinate having multiple items
                # (why we created the list), we need to return them in
                # ascending order.
                order_mapping[column][row].sort()
                tr.extend(order_mapping[column][row])
            result.append(tr)
        return result

    def helper(self, node: Optional[TreeNode], row: int, col: int, node_order_mapping: dict):
        # Simple pre order traversal:
        # If we've gone past a leaf, we're done with this recursive
        # call.
        if not node:
            return
        else:
            # Add the current node to the mapping/hash table.
            # Note that we nest by column, then row, while the
            # convention is row, column!
            # This is because row, column is more familiar to most
            # people, but the problem is more easily solved by going
            # column, row.
            node_order_mapping[col][row].append(node.val)
            # Then get its left subtree, whose root is at
            # (row+1, col-1) because it's one row deeper but one column
            # to the left
            self.helper(node.left, row+1, col-1, node_order_mapping)
            # Then get its right subtree, whose root is at
            # (row+1, col+1), because it's one row deeper, like the
            # right ST, but one column to the right
            self.helper(node.right, row+1, col+1, node_order_mapping)
            # No return because we mutate the hash table in each
            # recursive call.
            # (Functional programmers would hate this but it's NBD. We
            # can refactor it later)
