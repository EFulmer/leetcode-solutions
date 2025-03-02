# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Pretty simple idea:
        # If both lists are null, return null,
        # If only one list is null, return the other.
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        # Otherwise, keep going through the lists, and at each step
        # compare the "remaining"
        # (i.e. we move our pointer up once an item is used)
        # head pointers of the lists.
        # If the value of l1's head node is smaller, append that value
        # to the end of our new sorted_list
        # Otherwise, append the value of l2's head node.
        # And advance the pointer on the list whose head was smaller.
        l1p, l2p = list1, list2
        if l1p.val < l2p.val:
            sorted_list_head = ListNode(val=l1p.val)
            l1p = l1p.next
        else:
            sorted_list_head = ListNode(val=l2p.val)
            l2p = l2p.next

        sorted_list_cur = sorted_list_head
        while l1p is not None and l2p is not None:
            if l1p.val < l2p.val:
                sorted_list_cur.next = ListNode(val=l1p.val)
                sorted_list_cur = sorted_list_cur.next
                l1p = l1p.next
            else:
                sorted_list_cur.next = ListNode(val=l2p.val)
                sorted_list_cur = sorted_list_cur.next
                l2p = l2p.next

        # Once one list is exhausted, copy the rest of the non-exhausted
        # list onto our new, master sorted list, as-is.
        copy_remaining_list(sorted_list_cur, l1p, l2p)
        return sorted_list_head


def copy_remaining_list(
    sorted_list_cur: Optional[ListNode],
    list1: Optional[ListNode],
    list2: Optional[ListNode],
) -> None:
    if list1 is None:
        list_pointer = list2
    else:
        list_pointer = list1

    while list_pointer is not None:
        sorted_list_next = ListNode(list_pointer.val)
        sorted_list_cur.next = sorted_list_next
        sorted_list_cur = sorted_list_next
        list_pointer = list_pointer.next


# Second solution: using a queue (better CPU performance)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases:
        # 1. Both lists are empty.
        # 2. list1 is empty.
        # 3. list2 is empty.
        # Handling them in order:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        # Otherwise, queue-based approach: append the smallest item to
        # the head of the queue and advance the pointer to its list.
        l1_ptr, l2_ptr = list1, list2
        vals = deque(maxlen=100)
        if l1_ptr.val < l2_ptr.val:
            vals.append(l1_ptr.val)
            l1_ptr = l1_ptr.next
        else:
            vals.append(l2_ptr.val)
            l2_ptr = l2_ptr.next

        while l1_ptr is not None and l2_ptr is not None:
            if l1_ptr.val < l2_ptr.val:
                vals.append(l1_ptr.val)
                l1_ptr = l1_ptr.next
            else:
                vals.append(l2_ptr.val)
                l2_ptr = l2_ptr.next

        remaining_ptr = l1_ptr if l2_ptr is None else l2_ptr

        while remaining_ptr is not None:
            vals.append(remaining_ptr.val)
            remaining_ptr = remaining_ptr.next

        head = ListNode(val=vals.popleft())
        sorted_next = head.next = ListNode(val=vals.popleft())

        while len(vals) > 0:
            sorted_next.next = ListNode(val=vals.popleft())
            sorted_next = sorted_next.next
        return head
