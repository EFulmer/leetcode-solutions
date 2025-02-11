class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        substring_length = len(part)
        lp = list(part)
        for char in s:
            stack.append(char)
            if stack[-substring_length:] == lp:
                for i in range(substring_length):
                    stack.pop()
        if stack[-substring_length:] == lp:
            for i in range(substring_length):
                stack.pop()
        return "".join(stack)
