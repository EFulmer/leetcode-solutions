# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif all(l is None for l in lists):
            return None
        # Just heapsort it.
        heap = []
        for lst in lists:
            current_list_head = lst
            while current_list_head is not None:
                heapq.heappush(heap, current_list_head.val)
                current_list_head = current_list_head.next
        result_head = ListNode(heapq.heappop(heap))
        result_tail = result_head
        while len(heap) > 0:
            result_tail.next = ListNode(heapq.heappop(heap))
            result_tail = result_tail.next
        return result_head
