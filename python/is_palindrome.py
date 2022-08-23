# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # two traversals:
        # first, accumulate a stack of the values
        # then see if the stack matches
        pointer_1 = head
        acc = []
        while pointer_1:
            acc.append(pointer_1.val)
            pointer_1 = pointer_1.next
        pointer_2 = head
        while pointer_2:
            if acc.pop() != pointer_2.val:
                return False
            else:
                pointer_2 = pointer_2.next
        return True
