class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        high = max(ranks) * cars ** 2
        while low < high:
            mid = (high + low) // 2
            if can_repair_cars_in(ranks, cars, mid):
                high = mid
            else:
                low = mid + 1
        return low


def can_repair_cars_in(ranks: List[int], cars: int, minutes: int) -> bool:
    # For each mechanic, how many cars can they repair within the
    # specified number of minutes?
    # If the sum of that is >= the number of cars we really have, True,
    # else False.
    #
    # time a mechanic takes to repair N cars = rank * n ** 2
    # We need to solve for how many cars each mechanic can repair
    # in the given time.
    # Rewrite it: time = rank * n ** 2 == n ** 2 = time / rank
    # n = sqrt(time / rank)
    # if # of cars that everyone can clean >= the number
    # we NEED to clean?
    result = 0
    for rank in ranks:
        result += math.floor((minutes / rank) ** 0.5)
    return result >= cars
