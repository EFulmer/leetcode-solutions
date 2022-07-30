from collections import Counter


class Solution:
    def make_super_counter(self, words2: List[str]) -> Counter:
        """Merge all words in the second words collection to make a singular Counter that counts all of them.
        The "Super Counter" includes the maximum count of each letter across every
        word in `words2`; i.e. if words2 = ["wrr", "wa", "or"],
        we get Counter({"w": 1, "r": 2, "a": 1, "o": 1})
        """
        counter = Counter(words2[0])
        for i in range(1, len(words2)):  # avoid slicing as that makes a copy
            current_word = Counter(words2[i])
            for char in current_word.keys():
                if current_word[char] > counter[char]:
                    counter[char] = current_word[char]
        return counter

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result = []
        counter = self.make_super_counter(words2)
        for word in words1:
            current_word = Counter(word)
            for char, count in counter.items():
                if char not in current_word.keys():
                    break
                elif count > current_word[char]:
                    break
            else:
                result.append(word)
        return result
