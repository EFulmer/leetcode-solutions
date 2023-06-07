DIGITS_TO_LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = [c for c in DIGITS_TO_LETTERS[digits[0]]]
        for d in digits[1:]:
            results = [
                r + c
                for r in results
                for c in DIGITS_TO_LETTERS[d]
            ]
        return results
