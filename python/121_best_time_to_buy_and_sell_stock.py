class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Logic:
        # You want to buy on the day with the lowest price possible
        # and sell on the future day with the highest price possible.
        # Using that, I sketch out an algorithm:
        # worst case: we never buy anything, profit of 0.
        # Look at each day's price in order; if today has the lowest
        # price you've seen so far, it's the best day so far to buy on.
        # If not, does it make sense to sell on that day?
        # Check that by checking whether:
        # prices[d] - mininum price before i > best profit before d
        min_price_seen = float("inf")
        profit = 0
        for i in prices:
            if i < min_price_seen:
                min_price_seen = i
            elif i - min_price_seen > profit:
                profit = i - min_price_seen
        return profit
