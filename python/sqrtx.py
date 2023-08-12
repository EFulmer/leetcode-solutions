step = lambda guess, x: guess - ( (guess**2 - x)/ (2 * guess))

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        # Let's try doing Newton's Method.
        guess = x // 2
        new_guess = step(guess, x)
        while abs(new_guess - guess) > 0.01:
            guess = new_guess
            new_guess = step(guess, x)
        return int(new_guess)
