# High memory usage solution:
# Initialize two sets, for keeping track of which numbers you have seen
# in A and B, respectively.
# The common prefix is the size of their intersection.
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        result = [0] * N
        seen_in_A = set()
        seen_in_B = set()
        for i in range(0, N):
            seen_in_A.add(A[i])
            seen_in_B.add(B[i])
            result[i] = len(seen_in_A & seen_in_B)
        return result


# More efficient:
# Keep track of how many times you have seen each element. Once it
# hits 2, increment.
# Could use a list and either accept that it will have N+1 items,
# or have counts[i] = number of times i+1 has been seen so far
# but I prefer the semantic intent that a dictionary conveys.
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        result = [0] * N
        counts = {i: 0 for i in range(1, N+1)}
        for i in range(N):
            a, b = A[i], B[i]
            result[i] = result[i-1]

            counts[a] += 1
            if counts[a] == 2:
                result[i] += 1

            counts[b] += 1
            if counts[b] == 2:
                result[i] += 1

        return result


# Solution as above, but with the index arithmetic mentioned in my
# explanation:
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        result = [0] * N
        counts = [0] * N
        for i in range(N):
            a, b = A[i], B[i]
            result[i] = result[i-1]

            counts[a-1] += 1
            if counts[a-1] == 2:
                result[i] += 1

            counts[b-1] += 1
            if counts[b-1] == 2:
                result[i] += 1

        return result
