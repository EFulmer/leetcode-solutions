class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # maybe dict instead?
        openers = ["(", "[", "{"]
        closers = [")", "]", "}"]
        parens = dict(zip(openers, closers))
        for c in s:
            if c in openers:
                stack.append(c)
            elif c in closers:
                if not stack or parens[stack[-1]] != c:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
