from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        # The data transformation desired is:
        # collect the sums of digits of each number
        # i.e.
        # nums = [18, 43, 36, 13, 7]
        # sum of digits = [9, 7, 9, 4, 7]
        # sums of digits mapped to actual values in nums:
        # { 4: [13], 7: [43, 13], 9: [18, 36] }
        # then find out of each of those sums that has >= 2 n in nums
        # associated with it, what's the greatest sum?
        digit_sums_to_nums = get_digit_sum_mapping(nums)
        result = -1
        for ns in digit_sums_to_nums.values():
            if len(ns) < 2:
                continue
            contender = sum(sorted(ns)[-2:])
            result = max(result, contender)
        return result


def get_digit_sum_mapping(nums: List[int]) -> Dict[int, List[int]]:
    """Make a dictionary (technically, a defaultdict) mapping digit
    sums of the values of nums to the values themselves.
    """
    digit_sums_to_nums = defaultdict(list)
    for num in nums:
        ds = digit_sum(num)
        digit_sums_to_nums[ds].append(num)
    return digit_sums_to_nums


def digit_sum(x: int) -> int:
    """Calculate the sum of the digits of x."""
    return sum(int(c) for c in str(x))
