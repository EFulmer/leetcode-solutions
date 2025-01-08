def is_prefix_and_suffix(candidate: str, word: str) -> bool:
    if len(candidate) > len(word):
        return False
    return word.startswith(candidate) and word.endswith(candidate)


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        n = len(words)
        for i in range(0, n-1):
            for j in range(i+1, n):
                result += is_prefix_and_suffix(candidate=words[i], word=words[j])
        return result
