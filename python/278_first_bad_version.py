# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # This is literally just binary search, with an additonal piece
        # of information: We know the answer in our collection.
        low = 0
        high = n
        while True:
            mid = (high + low) // 2
            # Case 1: It's at a higher version number
            if not isBadVersion(mid):
                low = mid + 1
            # Case 2: We've found it.
            elif isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            # Case 3: A bad version, but not the first bad version.
            else:
                high = mid
