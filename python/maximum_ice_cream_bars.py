class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # hard code some early termination cases
        if coins >= sum(costs):
            return len(costs)
        elif coins < min(costs):
            return 0
        result = 0
        for i in sorted(costs):
            if i > coins:
                break
            else:
                result += 1
                coins -= i
        return result
