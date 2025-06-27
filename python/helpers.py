from collections import deque
from math import log10, trunc
from typing import List, Optional


class ListNode(object):
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def list_to_ll(l: List) -> Optional[ListNode]:
    # empty pointer for simplicity
    result = ListNode()
    cur = result
    for item in l:
        cur.next = ListNode(item)
        cur = cur.next
    return result.next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"


def num_digits_in_int(n: int) -> int:
    return trunc(log10(n)) + 1


def list_of_ints_to_int(l: List[int]) -> int:
    m = len(l)
    return sum(
        n * 10**(m-i-1)
        for i, n in enumerate(l)
    )


def list_of_digits(x):
    l = num_digits_in_int(x)
    result = []
    while l > 0:
        current_digit = x // 10**(l-1)
        result.append(current_digit)
        x = x - (current_digit * 10**(l-1))
        l -= 1
    return result


def knapsack(weights: list, values: list, capacity: int):
    if len(values) != len(weights):
        raise ValueError("should be one weight and value per item, no more, no less")
    solutions = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    for i in range(len(weights)):
        for w in range(capacity+1):
            if weights[i] <= w:
                solutions[i+1][w] = max(
                    solutions[i][w],
                    solutions[i][w - weights[i]] + values[i],
                )
            else:  # Exclude branch
                solutions[i+1][w] = solutions[i][w]
    return solutions


def shift_one_character_by(char: str, d: int) -> str:
    """Shift the ASCII lowercase char, `char` by `d` positions in the
    Latin alphabet.
    """
    # NOT `char`'s ASCII value,
    # but rather its index in `string.ascii_lowercase`.
    char_number = ord(char) - 97
    return string.ascii_lowercase[(char_number + d) % 26]


def edges_to_adjacency_list(edges: list[list[int]]) -> dict[int, list[int]]:
    """Convert a list of pairs (edges) to an adjacency list
    representation of a graph.
    """
    # TODO add directed option
    adjacency_list = dict()
    for (v1, v2) in edges:
        if v1 not in adjacency_list.keys():
            adjacency_list[v1] = [v2]
        else:
            adjacency_list[v1].append(v2)
        if v2 not in adjacency_list.keys():
            adjacency_list[v2] = [v1]
        else:
            adjacency_list[v2].append(v1)
    return adjacency_list


def dfs_adjacency_list(adjacency_list):
    """Reference implementation for DFS through adjacency lists."""
    queue = deque()
    seen = set()
    queue.append(0)
    while len(queue) > 0:
        current = queue.popleft()
        seen.add(current)
        print(f"{current = }")
        for neighbor in adjacency_list[current]:
            if neighbor not in seen:
                queue.append(neighbor)
    return


def backtracking_helper(data, success_pred, failure_pred, partial_solution):
    # If the current partial solution satisfies the criteria, it is no
    # longer a "partial" solution. Yield it.
    if success_pred(partial_solution):
        yield partial_solution
    # If it satisfies the failure predicate, then it's not a solution at
    # all. Stop generation.
    elif failure_pred(partial_solution):
        return

    # Otherwise, we take the remaining data/input, check if the current
    # solution in flight can form a solution in combination with the
    # first item off of aforementioned remaining data, see if we can use
    # that + the rest of the remaining state to create a solution, and
    # then see if we can form a solution without using that first item
    # of the remaining data.
    for index, item in enumerate(data):
        # Try with the first item in the remaining data.
        partial_solution.append(item)
        yield from backtracking_helper(
            data=data[i:],
            success_pred=success_pred,
            failure_pred=failure_pred,
            partial_solution=partial_solution,
        )
        # Then check for solutions that don't use it.
        partial_solution.pop()


def combination_sum(candidates: int, target: int):
    # TODO: future improvements: remove repeated copying of input data,
    # default value for partial_solution,
    # handle other sorts of input collections aside that which we
    # can index like a list.
    success_pred = lambda x: sum(x) == target
    failure_pred = lambda x: sum(x) > target
    yield from backtracking_helper(
        data=candidates,
        success_pred=success_pred,
        failure_pred=failure_pred,
        partial_solution=[],
    )
