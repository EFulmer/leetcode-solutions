class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        costs = [0] * n

        moves_from_left = moves_from_right = 0
        balls_to_left   = balls_to_right   = 0

        for i in range(n):
            # Handle the left and right cases separately.
            left_pointer = i
            # We know how many boxes are being brought in from our
            # "left side", and we don't count any ball that may already
            # be in this box since it doesn't need to be moved.
            costs[i] += moves_from_left
            # If there's a ball in this box, we increment the number of
            # balls and moves to be made from the left.
            # Could exploit that in Python, False == 0, but using an
            # if statement is clearer.
            if boxes[left_pointer] == '1':
                balls_to_left += 1
            # Setting up the next iteration:
            # We add one move from the left for each ball to our left
            # at this index, since we need one operation to move each
            # ball closer to its final destination at left_pointer.
            moves_from_left += balls_to_left

            # Right case. Follows the same idea as the left.
            right_pointer = n - i - 1
            costs[right_pointer] += moves_from_right
            if boxes[right_pointer] == '1':
                balls_to_right += 1
            moves_from_right += balls_to_right
        return costs
