class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # cost array = how much gas it costs to get from this station to the next
        # gas array = how much gas avail. at this station
        # thoughts:
        # 1. try starting at the station with the most gas (max(gas))
        # 2. try starting at the station closest to the next (min(cost))
        # attempting 1 first
        if sum(gas) < sum(cost):
            return -1

        stations_and_indices = list(enumerate(gas))
        # sort by the amount of gas they have
        stations_and_indices.sort(key=lambda x: x[1], reverse=True)
        for i, _ in stations_and_indices:
            if self.can_start_from(gas=gas, cost=cost, start=i):
                return i
        return -1

    def can_start_from(self, gas: List[int], cost: List[int], start: int) -> bool:
        n = len(cost)
        idx = start
        tank = 0
        for _ in range(n):
            # fuel up
            tank = tank + gas[idx]
            # then drive
            tank = tank - cost[idx]
            if tank < 0:
                return False
            else:
                idx = (idx + 1) % n
        return True
