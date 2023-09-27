# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import log10, trunc

def ll_to_vector(ll: Optional[ListNode]) -> list:
    acc = []
    while ll:
        acc.append(ll.val)
        ll = ll.next
    return acc

def list_of_ints_to_int(l: List[int]) -> int:
    m = len(l)
    return sum(
        n * 10**(m-i-1)
        for i, n in enumerate(l)
    )

def num_digits_in_int(n: int) -> int:
    try:
        return trunc(log10(n)) + 1
    except ValueError:  # attempted log of 0
        return 1

def list_of_digits(x):
    l = num_digits_in_int(x)
    result = []
    while l > 0:
        current_digit = x // 10**(l-1)
        result.append(current_digit)
        x = x - (current_digit * 10**(l-1))
        l -= 1
    return result

def vector_to_ll(xs) -> ListNode:
    result = node = ListNode(xs[0], None)
    for i in range(1, len(xs)):
        node.next = ListNode(xs[i], None)
        node = node.next
    return result

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list_of_ints_to_int(list(reversed(ll_to_vector(l1))))
        n2 = list_of_ints_to_int(list(reversed(ll_to_vector(l2))))
        ans = n1 + n2
        return vector_to_ll(list(reversed(list_of_digits(ans))))
