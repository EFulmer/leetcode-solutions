# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty or one-node list
        if head is None or head.next is None:
            return head
        # The trick to doing this in an iterative manner is to track
        # the previous and next nodes, as well as the current node.
        # That way you can safely flip the current node's .next pointer
        # and also keep track of the next node in the original order,
        # which lets you iterate through the list.
        prev = None
        current = head
        next_ = None
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        # Since the condition of our while loop is current not being
        # null, we need to return the prev pointer! Returning current
        # or next_ returns a null pointer!
        return prev
