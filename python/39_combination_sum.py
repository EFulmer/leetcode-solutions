class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, partial_solution):
            if target == 0:
                result.append(partial_solution[:])
            elif target < 0:
                return

            i = start
            while i < len(candidates):
                partial_solution.append(candidates[i])
                backtrack(i, target - candidates[i], partial_solution)
                partial_solution.pop()
                i += 1

        backtrack(0, target, [])
        return result
