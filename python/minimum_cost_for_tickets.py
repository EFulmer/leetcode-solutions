def opt_naive(days, costs, *, current_day=1, current_cost=0):
    if current_day > max(days):
        return current_cost
    elif current_day not in days:
        return opt(
            days, costs, current_day=current_day+1, current_cost=current_cost
        )
    else:
        return min(
            opt(days, costs, current_day=current_day+1, current_cost=current_cost+costs[0]),
            opt(days, costs, current_day=current_day+7, current_cost=current_cost+costs[1]),
            opt(days, costs, current_day=current_day+30, current_cost=current_cost+costs[2])
        )


def opt_table(days, costs):
    # explicit dynamic programming approach
    # let dp[i] = minimum cost for all travel for days up to and including i
    # the worst case is if you buy a 30 day train pass every single day ever
    dp = [costs[-1] * i for i in range(max(days)+1)]
    i = 1
    while i < len(dp):
        # if there is no travel to be done on day i, then we can fill the table up from i...(next travel day, not inclusive)
        # with the cost of the last travel day
        # then jump to the next travel day
        if i not in days:
            # if the first travel day is not day 1, we may run into an IndexError here
            # in that case, we should be able to safely zero out everything up to, but not including
            # the first travel day
            try:
                last_travel_day = [day for day in days if day < i][-1]
            except IndexError:
                last_travel_day = 0
            next_travel_day = [day for day in days if day > i][0]
            for day in range(last_travel_day, next_travel_day):
                dp[day] = dp[last_travel_day]
            i = next_travel_day
        else:
            # We want to get the best price if we bought a 1-day pass in any of the days before
            # compared to a 7-day pass,
            # compared to a 30-day pass
            candidates = [
                dp[i-1] + costs[0],
                dp[max(0, i-7)] + costs[1],
                dp[max(0, i-30)] + costs[2]
            ]
            dp[i] = min(candidates)
            i += 1
    return dp


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return opt_table(days, costs)[-1]
