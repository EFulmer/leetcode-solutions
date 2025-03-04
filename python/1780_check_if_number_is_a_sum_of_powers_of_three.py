class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Enumerate all the powers of three
        # Repeatedly subtract them from `n` until we can't anymore.
        # 3 ** 15 is the largest power of three that is less than 10**7
        # (which is the maximum input)
        # Skipping 1 since we check for 1 at the end.
        powers_of_three = [3**i for i in range(15, 0, -1)]
        while n >= 3:
            i = 0
            while i < len(powers_of_three):
                if n >= powers_of_three[i]:
                    n -= powers_of_three[i]
                    break
                else:
                    i += 1
            if i == len(powers_of_three):
                break
            else:
                powers_of_three.pop(i)
        return n == 1 or n == 0
