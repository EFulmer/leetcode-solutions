import re


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # In order for a move to be made, the player needs 3 of their
        # "color"; so they can remove the center of those 3.
        # Assuming that both make optimal moves, the number of
        # triplets won't decrease between iterations so we can use
        # the count from the start.
        alice_count = sum(1 for _ in re.finditer("(?=AAA)", colors))
        bob_count = sum(1 for _ in re.finditer("(?=BBB)", colors))
        return alice_count > bob_count
