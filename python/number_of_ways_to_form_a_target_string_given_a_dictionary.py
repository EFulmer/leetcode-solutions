class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        modulo = 10 ** 9 + 7
        word_length = len(words[0])
        target_length = len(target)

        # list of dicts:
        # frequencies[i] = how many times char appears in column i
        frequencies = [dict() for _ in range(word_length)]
        for word in words:
            for i, char in enumerate(word):
                frequencies[i][char] = frequencies[i].get(char, 0) + 1

        # only need to track the last iteration in this dynamic
        # programming problem
        # previous_combos[i] = number of ways to form target_length[:i]
        # from the given words
        # p[0] = 1 since target_length[:0] is the empty string
        previous_combos = [0 for _ in range(target_length+1)]
        previous_combos[0] = 1
        current_combos = [0 for _ in range(target_length+1)]
        # for each word, and each char of each word, you can form
        # target[:i] by either using one of the times target[i-1]
        # appears at that index in any word (frequencies gives you the
        # count here), or not using it and moving on to the next letter
        for word_index in range(word_length):
            current_combos = previous_combos[:]
            for i, char in enumerate(target, start=1):
                current_combos[i] = current_combos[i] + \
                    frequencies[word_index].get(char, 0) * previous_combos[i-1]
                current_combos[i] = current_combos[i] % modulo
            previous_combos = current_combos[:]
        return current_combos[target_length]
