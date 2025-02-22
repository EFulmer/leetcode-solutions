# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        length = 0
        while runner is not None:
            runner = runner.next
            length += 1
        midpoint = length // 2
        mid_finder = head
        i = 0
        while i < midpoint:
            mid_finder = mid_finder.next
            i += 1
        return mid_finder
