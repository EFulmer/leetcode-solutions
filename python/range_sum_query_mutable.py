class NumArray:

    def __init__(self, nums: List[int]):
        # Creating a segment tree stored in an array:
        # need an array of 2*len(n), since the input array is the
        # segment tree's leaves
        self.n = len(nums)
        self.internal_tree = [0 for _ in range(self.n)] + nums[:]
        # construct the tree
        self._construct_tree()

    def _construct_tree(self) -> None:
        # each internal node is the parent of a leaf, or element of
        # the array argument nums
        # self.internal_tree[i*2] = nums[i]
        # self.internal_tree[i] = self.internal_tree[i*2] + self.internal_tree[i*2+1]
        # percolate "backwards" to i=0
        i = self.n - 1
        while i >= 0:
            left_child = i*2
            right_child = i*2 + 1
            self.internal_tree[i] = self.internal_tree[left_child] + self.internal_tree[right_child]
            i -= 1

    def update(self, index: int, val: int) -> None:
        # Unsure about this one;
        # as described in the constructor's comments, we need to shift up by n
        # to get to the leaf
        # then rebuild that subtree
        i = self.n + index
        self.internal_tree[i] = val
        self._reconstruct_subtree(i)

    def _reconstruct_subtree(self, leaf_index: int) -> None:
        # starting from leaf_index (which should be index+self.n passed into update)
        # we reconstruct that subtree to reflect the new leaf
        current_node = leaf_index
        while current_node > 0:
            left_child = current_node
            right_child = current_node
            # if the node we're updating at this iteration has an even index,
            # then right = ci*2+1
            # if it's odd, then left = ci*2-1
            # because we're actually updating current_node//2
            if current_node % 2 == 0:
                right_child = current_node + 1
            else:
                left_child = current_node - 1
            self.internal_tree[current_node//2] = self.internal_tree[left_child] + self.internal_tree[right_child]
            current_node //= 2

    def sumRange(self, left: int, right: int) -> int:
        # left and right point to leaves (after shifting them)
        left, right = left + self.n, right + self.n
        # to get the sum, add up the right ancestors of left (since the if left's parent is its' grandparent's left child, left.parent.parent.left is out of the range)
        # and the left ancestors of right
        # (leaves and internal)
        # on their common subtree
        result = 0
        while left <= right:
            # some handling of evens and odds
            if left % 2 == 1:
                result += self.internal_tree[left]
                left += 1
            if right % 2 == 0:
                result += self.internal_tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
