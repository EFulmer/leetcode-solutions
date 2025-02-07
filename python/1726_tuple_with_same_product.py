from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Logic:
        # For every quadruplet of numbers, there are eight possible
        # orderings.
        # So for each time we see a product, that's plus 8 to the
        # result.
        result = 0
        product_counts = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                current_product = nums[i] * nums[j]
                count = product_counts[current_product]
                result = result + (8 * count)
                product_counts[current_product] = count + 1

        return result
