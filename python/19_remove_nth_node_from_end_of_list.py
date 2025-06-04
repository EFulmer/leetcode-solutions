# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Approach (creates a new list):
        # Iterate through the list and put each value, in the same
        # order as they are in the OG list, into a vector/growable
        # array.
        # Delete the n-th from the end (in Python, index `-n`).
        # Turn the remaining items in the vector into a new linked list
        # Not sure why I named this one q...
        q = []
        length = 0
        cur = head
        while cur is not None:
            q.append(cur.val)
            length += 1
            cur = cur.next
        q.pop(-n)
        if not q:
            return
        result = ListNode(q.pop(0))
        result_pointer = result
        while q:
            result_pointer.next = ListNode(q.pop(0))
            result_pointer = result_pointer.next
        return result
