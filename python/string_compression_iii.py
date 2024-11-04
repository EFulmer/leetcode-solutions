import dataclasses
import itertools


@dataclasses.dataclass
class Run:
    character: str
    length: int

def get_run_and_length(word, index):
    character = word[index]
    it = itertools.takewhile(lambda l: l == character, word[index+1:])
    length = 1
    for _ in it:
        length += 1
        if length == 9:
            break
    return Run(character=character, length=length)


class Solution:
    def compressedString(self, word: str) -> str:
        acc = []
        result = ""
        index = 0
        length = len(word)
        while index < length:
            current_run = get_run_and_length(word, index)
            acc.append(current_run)
            index += current_run.length
        return "".join(f"{run.length}{run.character}" for run in acc)
