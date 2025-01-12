# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_pointer = head

        if fast_pointer is None:
            return False

        fast_pointer = head.next
        slow_pointer = head
        while fast_pointer is not None:
            try:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            except Exception as e:
                break
            if fast_pointer is slow_pointer:
                return True
        return False
