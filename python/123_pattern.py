class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # We're looking for intervals satisfying the property:
        # nums[i] < nums[k] < nums[j] and i < j < k
        # Our initial "interval" is just (nums[0], nums[0]),
        # which doesn't satisfy anything, but that's fine, we just
        # need a starting interval.
        stack = [(nums[0], nums[0])]
        # Now loop through the rest of the array
        # (i.e. starting at nums[1]):
        for i in range(1, len(nums)):
            num = nums[i]
            # We start a new interval on the stack in two cases:
            # 1. The stack is empty so any interval (nums[i], nums[i])
            # would "work"
            # 2. The current number (nums[i]) is less than the min
            # bound of the top interval on the stack
            if len(stack) == 0 or num < stack[-1][0]:
                stack.append((num, num))
            else:
                # If there's stuff on the stack we look and see
                # if any interval on the stack would form a valid
                # triple with the current item in the array:
                lower_bound = stack[-1][0]
                while len(stack) != 0 and stack[-1][1] < num:
                    stack.pop()
                # Now that we've found the maximum contender for #2 in
                # the triple (or exhausted the stack), we check if it
                # fits the property. If it does, we're done. If not,
                # add the pair formed by the lower bound and the current
                # number and continue.
                if len(stack) != 0 and stack[-1][0] < num < stack[-1][1]:
                    return True
                else:
                    stack.append((lower_bound, num))
        return False
