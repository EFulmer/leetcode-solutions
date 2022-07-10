class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        current_minimum_cost = 0
        candidate_1 = cost[0]
        candidate_2 = cost[1]
        for i in range(2, len(cost)):
            current_minimum_cost = cost[i] + min(candidate_1, candidate_2)
            candidate_1 = candidate_2
            candidate_2 = current_minimum_cost
        return min(candidate_1, candidate_2)
