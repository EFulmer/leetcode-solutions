class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        if not tasks:
            return 0
        tasks = Counter(tasks)
        if 1 in tasks.values():
            return -1
        rounds = 0
        # Rather than iterating each round, let's count how many rounds
        # it'll take to complete all tasks of a given priority.
        # This (count + 2) / 3 works because if count's even and
        # indivisible by 3, doing 3 or 2 each round doesn't change the
        # # of rounds
        # so it's "pushing count up" to the proper rounding threshold
        rounds = sum(int((count + 2) / 3) for count in tasks.values())
        return rounds
