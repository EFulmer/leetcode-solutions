class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # brute-force:
        # for each word; check if it's a substring of every other word
        # we can slightly speed it up by sorting the words by length
        words = sorted(words, key=len)
        n = len(words)
        result = []
        for i in range(n-1):
            current_word = words[i]
            for j in range(i+1, n):
                if current_word in words[j]:
                    result.append(current_word)
                    break
        return result
