# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Finding middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # Reversing the second part
        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        curr1 = head
        curr2 = prev

        while curr2:
            nxt1 = curr1.next
            curr1.next = curr2
            curr1 = nxt1

            nxt2 = curr2.next
            curr2.next = nxt1
            curr2 = nxt2

        