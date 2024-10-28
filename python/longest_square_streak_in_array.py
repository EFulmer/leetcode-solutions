def find_ss(nums, setnums, start=0):
    # Fourth version, use a set rather than naively loop through the whole list
    if start == len(nums)-1:
        return None
    cand = [nums[start]]
    last = cand[-1]
    while len(cand) < 6 and (last**2 in setnums):
        cand.append(last**2)
        last = cand[-1]
    if len(cand) < 2:
        return None
    return cand


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(nums)
        setnums = set(nums)
        square_streaks = [find_ss(nums, setnums, start=i) for i in range(len(nums))]
        square_streaks = [ss for ss in square_streaks if ss]
        if square_streaks:
            ss_lens = [len(s) for s in square_streaks]
            return sorted(ss_lens, reverse=True)[0]
        return -1
