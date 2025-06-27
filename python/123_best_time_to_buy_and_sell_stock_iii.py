class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This is a classic dynamic programming problem.
        # At any given moment, there are two variables controlling
        # the "status" of the DP problem:
        # 1. Are you currently holding stock? (Boolean)
        # 2. How many trades have been performed?
        #
        # To communicate the algorithm a little more clearly,
        # I make an enum for those.
        HOLDING = 1
        NOT_HOLDING = 0
        # Initialize states:
        # 2D table: dimension 1 = # trades made, dim 2 = holding or not
        # dp[k][0] = max profit with k transactions and not holding
        # dp[k][1] = max profit with k transactions and holding
        # Base cases:
        # not holding = 0 profit,
        # holding = -∞ profit
        # (the -∞ is just for easy use of max function, but
        # it's technically correct as a worst possible case)
        dp = [[0, float("-inf")] for _ in range(3)]  # k = 0,1,2

        for price in prices:
            for trade_count in range(2, 0, -1):
                # Update for not holding (sell):
                # If you are not holding stock, either you just sold
                # or you haven't bought stock.
                # Those are arguments 1 and 2 to `max` respectively.
                dp[trade_count][NOT_HOLDING] = max(
                    dp[trade_count][NOT_HOLDING], dp[trade_count][HOLDING] + price
                )
                # Update for holding (buy):
                # If you are holding stock, either you just bought it
                # (arg 2 to `max`) or you bought it before and haven't
                # performed another transaction yet (arg 1)
                dp[trade_count][HOLDING] = max(
                    dp[trade_count][HOLDING], dp[trade_count-1][NOT_HOLDING] - price
                )

        # Since buying stock decreases your profit, the max profit is
        # had when you've sold.
        return dp[2][NOT_HOLDING]
