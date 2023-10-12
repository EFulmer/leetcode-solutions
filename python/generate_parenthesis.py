class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # You recursively build up a solution to n by taking the
        # solutions to n-1 and wrapping them in a pair and adding the
        # solutions to n-2 to the right of that.
        if n == 0:
            return [""]
        result = []
        for i in range(n):
            for back_1 in self.generateParenthesis(i):
                for back_2 in self.generateParenthesis(n-i-1):
                    result.append(f"({back_1}){back_2}")
        return result
