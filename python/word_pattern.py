class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split the string on its words, map each to a letter of the pattern (zip a word in s to a pattern in pattern)
        # if there's no duplicates then we have a match (a True)
        words = s.split()
        words_to_letters = {}
        letters_to_words = {}
        if len(words) != len(pattern):
            return False
        for p, w in zip(pattern, words):
            # If the current character has been seen before, we want to check what it maps to.
            # If it maps to another word than the current word, we can terminate early with False. (e.g. "a" would have to map to both "dog" and "cat", which isn't allowed, as that means this isn't a bijection.)
            if p in words_to_letters.keys():
                if w != words_to_letters[p]:
                    return False
            elif w in letters_to_words.keys():
                if p != letters_to_words[w]:
                    return False
            else:
                # If `p` is a "new" letter/pattern variable/etc., not seen before, enter it in the match tables connected to `w`
                words_to_letters[p] = w
                letters_to_words[w] = p
        # If we haven't found any contradictions (where either a word would be made to map to two letters or a letter would be made to map to two words), return True "by default"
        return True
