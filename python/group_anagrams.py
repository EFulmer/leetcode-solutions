from collections import defaultdict

class Solution:
    def make_hash_table(self, strs) -> Dict[str, List[str]]:
        result = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            result[ss].append(s)
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = self.make_hash_table(strs)
        result = []
        strs = set(strs)
        while strs:
            current_string = strs.pop()
            css = "".join(sorted(current_string))
            anagrams = ht.pop(css, [current_string])
            for anagram in anagrams:
                try:
                    strs.remove(anagram)
                except KeyError:
                    pass
            result.append(anagrams)
        return result
