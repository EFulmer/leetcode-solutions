class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # We can compute the result using two facts:
        # 1. x ^ x == 0
        # 2. 1's in higher columns are "better" for minimizing the
        # answer.
        # We work down, starting from most significant, using that.
        target_set_bits_count = count_set_bits(num2)
        result = num1
        current_set_bits_count = count_set_bits(result)
        if target_set_bits_count == current_set_bits_count:
            return result
        elif target_set_bits_count > current_set_bits_count:
            # go column to column, flipping 0's to 1, till we're at the right count
            current_column = 0
            while target_set_bits_count > current_set_bits_count:
                # check if current column's bit is 0.
                # If so, flip it and increment the CSBC.
                if result & (1 << current_column) == 0:
                    result = result | (1 << current_column)
                    current_set_bits_count += 1
                # Either way, move on.
                current_column += 1
        else:  # target_set_bits_count < current_set_bits_count
            # go column to column, flipping 1's to 0, till we're at the right count
            current_column = 0
            while target_set_bits_count < current_set_bits_count:
                # Check if current column's bit is 1.
                # If so, flip it and DECREMENT the CSBC.
                if result & (1 << current_column) != 0:
                    result = result & ~(1 << current_column)
                    current_set_bits_count -= 1
                # Either way, move on.
                current_column += 1
        return result


def count_set_bits(x: int) -> int:
    """Count the number of bits set to 1 in the binary representation
    of `x`.

    Uses Brian Kernighan's algorithm, which has an O(log n) time
    complexity.
    """
    count = 0
    while x != 0:
        x &= (x - 1)
        count += 1
    return count
