class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        # Set the ceiling as the size of the largest pile
        # since Koko cannot eat from more than one pile
        # per hour.
        high = max(piles)
        while low < high:
            rate = (low + high) // 2
            if can_finish_within(piles, h, rate):
                high = rate
            else:
                low = rate + 1
        return low


def can_finish_within(piles: List[int], hours: int, rate: int) -> bool:
    # Compute the number of hours it takes to eat all the bananas in
    # each pile. If the sum of those is <= hours, then we "win" (True).
    # We round up: ceiling(pile_size / rate)
    result = 0
    for pile in piles:
        result += math.ceil(pile / rate)
        # Short-circuit:
        if result > hours:
            return False
    return result <= hours
