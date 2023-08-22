import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            y = string.ascii_uppercase[(columnNumber-1) % 26]
            result.append(y)
            columnNumber = (columnNumber-1) // 26
        return "".join(reversed(result))
